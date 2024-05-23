# encoding: utf-8
"""Methods to compute representational similarity analysis (RSA)."""

import numpy as np
from joblib import Parallel, delayed
from scipy import stats

from .folds import create_folds
from .rdm import _ensure_condensed, compute_rdm, compute_rdm_cv
from .searchlight import searchlight

try:
    # Version 1.8.0 and up
    from scipy.stats._stats_py import _kendall_dis
except ImportError:
    from scipy.stats.stats import _kendall_dis


def _kendall_tau_a(x, y):
    """Compute Kendall's Tau metric, A-variant.

    Taken from scipy.stats.kendalltau and modified to be the tau-a variant.
    """
    x = np.asarray(x).ravel()
    y = np.asarray(y).ravel()

    if x.size != y.size:
        raise ValueError(
            "All inputs to `kendalltau` must be of the same size,"
            " found x-size %s and y-size %s" % (x.size, y.size)
        )
    elif not x.size or not y.size:
        return np.nan  # Return NaN if arrays are empty

    def count_rank_tie(ranks):
        cnt = np.bincount(ranks).astype("int64", copy=False)
        cnt = cnt[cnt > 1]
        return (
            (cnt * (cnt - 1) // 2).sum(),
            (cnt * (cnt - 1.0) * (cnt - 2)).sum(),
            (cnt * (cnt - 1.0) * (2 * cnt + 5)).sum(),
        )

    size = x.size
    perm = np.argsort(y)  # sort on y and convert y to dense ranks
    x, y = x[perm], y[perm]
    y = np.r_[True, y[1:] != y[:-1]].cumsum(dtype="intp")

    # stable sort on x and convert x to dense ranks
    perm = np.argsort(x, kind="mergesort")
    x, y = x[perm], y[perm]
    x = np.r_[True, x[1:] != x[:-1]].cumsum(dtype="intp")

    dis = _kendall_dis(x, y)  # discordant pairs

    obs = np.r_[True, (x[1:] != x[:-1]) | (y[1:] != y[:-1]), True]
    cnt = np.diff(np.nonzero(obs)[0]).astype("int64", copy=False)

    ntie = (cnt * (cnt - 1) // 2).sum()  # joint ties
    xtie, x0, x1 = count_rank_tie(x)  # ties in x, stats
    ytie, y0, y1 = count_rank_tie(y)  # ties in y, stats

    tot = (size * (size - 1)) // 2

    if xtie == tot or ytie == tot:
        return np.nan

    # Note that tot = con + dis + (xtie - ntie) + (ytie - ntie) + ntie
    #               = con + dis + xtie + ytie - ntie
    con_minus_dis = tot - xtie - ytie + ntie - 2 * dis
    tau = con_minus_dis / tot
    # Limit range to fix computational errors
    tau = min(1.0, max(-1.0, tau))

    return tau


def _consolidate_masks(masks):
    if type(masks[0]) == slice:
        mask = slice(None)
    else:
        mask = masks[0]
        for m in masks[1:]:
            mask &= m
    return mask


def _partial_correlation(rdm_data, rdm_model, masks=None, type="pearson"):
    """Compute partial Pearson/Spearman correlation."""
    if len(rdm_model) == 1:
        raise ValueError(
            "Need more than one model RDM to use partial " "correlation as metric."
        )
    if type not in ["pearson", "spearman"]:
        raise ValueError("Correlation type must be either 'pearson' or " "'spearman'")

    if masks is not None:
        mask = _consolidate_masks(masks)
        rdm_model = [rdm[mask] for rdm in rdm_model]
        rdm_data = rdm_data[mask]

    X = np.vstack([rdm_data] + rdm_model).T
    if type == "spearman":
        X = np.apply_along_axis(stats.rankdata, 0, X)
    X = X - X.mean(axis=0)
    cov_X_inv = np.linalg.pinv(X.T @ X)
    norm = np.sqrt(np.outer(np.diag(cov_X_inv), np.diag(cov_X_inv)))
    R_partial = cov_X_inv / norm
    return -R_partial[0, 1:]


def rsa_gen(rdm_data_gen, rdm_model, metric="spearman", ignore_nan=False):
    """Generate RSA values between data and model RDMs.

    Will yield RSA scores for each data RDM.

    Parameters
    ----------
    rdm_data_gen : generator of ndarray, shape (n_items, n_items)
        The generator for data RDMs
    rdm_model : ndarray, shape (n_items, n_items) | list of ndarray
        The model RDM, or list of model RDMs.
    metric : str
        The RSA metric to use to compare the RDMs. Valid options are:

        * 'spearman' for Spearman's correlation (the default)
        * 'pearson' for Pearson's correlation
        * 'kendall-tau-a' for Kendall's Tau (alpha variant)
        * 'partial' for partial Pearson correlations
        * 'partial-spearman' for partial Spearman correlations
        * 'regression' for linear regression weights

        Defaults to 'spearman'.
    ignore_nan : bool
        Whether to treat NaN's as missing values and ignore them when computing the
        distance metric. Defaults to ``False``.

        .. versionadded:: 0.8

    Yields
    ------
    rsa_val : float | ndarray, shape (len(rdm_model),)
        For each data RDM, the representational similarity with the model RDM. When
        multiple model RDMs are specified, this will be a 1D array of similarities,
        comparing the data RDM with each model RDM.

    See Also
    --------
    rsa

    """
    if isinstance(rdm_model, list):
        return_array = True
        rdm_model = [_ensure_condensed(rdm, "rdm_model") for rdm in rdm_model]
    else:
        return_array = False
        rdm_model = [_ensure_condensed(rdm_model, "rdm_model")]

    if ignore_nan:
        masks = [~np.isnan(rdm) for rdm in rdm_model]
    else:
        masks = [slice(None)] * len(rdm_model)

    for rdm_data in rdm_data_gen:
        rdm_data = _ensure_condensed(rdm_data, "rdm_data")
        if ignore_nan:
            data_mask = ~np.isnan(rdm_data)
            masks = [m & data_mask for m in masks]
        rsa_vals = _rsa_single_rdm(rdm_data, rdm_model, metric, masks)
        if return_array:
            yield np.asarray(rsa_vals)
        else:
            yield rsa_vals[0]


def _rsa_single_rdm(rdm_data, rdm_model, metric, masks):
    """Compute RSA between a single data RDM and one or more model RDMs."""
    if metric == "spearman":
        rsa_vals = [
            stats.spearmanr(rdm_data[mask], rdm_model_[mask])[0]
            for rdm_model_, mask in zip(rdm_model, masks)
        ]
    elif metric == "pearson":
        rsa_vals = [
            stats.pearsonr(rdm_data[mask], rdm_model_[mask])[0]
            for rdm_model_, mask in zip(rdm_model, masks)
        ]
    elif metric == "kendall-tau-a":
        rsa_vals = [
            _kendall_tau_a(rdm_data[mask], rdm_model_[mask])
            for rdm_model_, mask in zip(rdm_model, masks)
        ]
    elif metric == "partial":
        rsa_vals = _partial_correlation(rdm_data, rdm_model, masks)
    elif metric == "partial-spearman":
        rsa_vals = _partial_correlation(rdm_data, rdm_model, masks, type="spearman")
    elif metric == "regression":
        mask = _consolidate_masks(masks)
        rdm_model = [rdm[mask] for rdm in rdm_model]
        rdm_data = rdm_data[mask]
        X = np.atleast_2d(np.array(rdm_model)).T
        X = X - X.mean(axis=0)
        y = rdm_data - rdm_data.mean()
        rsa_vals = np.linalg.lstsq(X, y, rcond=None)[0]
    else:
        raise ValueError(
            "Invalid RSA metric, must be one of: 'spearman', "
            "'pearson', 'partial', 'partial-spearman', "
            "'regression' or 'kendall-tau-a'."
        )
    return rsa_vals


def rsa(
    rdm_data,
    rdm_model,
    metric="spearman",
    ignore_nan=False,
    n_data_rdms=None,
    n_jobs=1,
    verbose=False,
):
    """Perform RSA between data and model RDMs.

    Parameters
    ----------
    rdm_data : ndarray, shape (n_items, n_items) | list | generator
        The data RDM (or list/generator of data RDMs).
    rdm_model : ndarray, shape (n_items, n_items) | list of ndarray
        The model RDM (or list of model RDMs).
    metric : str
        The RSA metric to use to compare the RDMs. Valid options are:

        * 'spearman' for Spearman's correlation (the default)
        * 'pearson' for Pearson's correlation
        * 'kendall-tau-a' for Kendall's Tau (alpha variant)
        * 'partial' for partial Pearson correlations
        * 'partial-spearman' for partial Spearman correlations
        * 'regression' for linear regression weights

        Defaults to 'spearman'.
    ignore_nan : bool
        Whether to treat NaN's as missing values and ignore them when computing
        the distance metric. Defaults to ``False``.

        .. versionadded:: 0.8
    n_data_rdms : int | None
        The number of data RDMs. This is useful when displaying a progress bar, so an
        estimate can be made of the computation time remaining. This information is
        available if ``rdm_data`` is an array or a list, but if it is a generator, this
        information is not available and you may want to set it explicitly.
    n_jobs : int
        The number of processes (=number of CPU cores) to use. Specify -1 to use all
        available cores. Defaults to 1.
    verbose : bool
        Whether to display a progress bar. In order for this to work, you need the tqdm
        python module installed. Defaults to False.

    Returns
    -------
    rsa_val : float | ndarray, shape (len(rdm_data), len(rdm_model))
        Depending on whether one or more data and model RDMs were specified, a single
        similarity value or a 2D array of similarity values for each data RDM versus
        each model RDM.

    See Also
    --------
    rsa_gen

    """
    return_array = False
    if isinstance(rdm_data, list) or hasattr(rdm_data, "__next__"):
        return_array = True
    else:
        rdm_data = [rdm_data]

    if verbose:
        from tqdm import tqdm

        if n_data_rdms is not None:
            total = n_data_rdms
        elif hasattr(rdm_data, "__len__"):
            total = len(rdm_data)
        else:
            total = None
        rdm_data = tqdm(rdm_data, total=total, unit="RDM")

    if n_jobs == 1:
        rsa_vals = list(rsa_gen(rdm_data, rdm_model, metric, ignore_nan))
    else:

        def process_single_rdm(rdm):
            return next(rsa_gen([rdm], rdm_model, metric, ignore_nan))

        rsa_vals = Parallel(n_jobs)(
            delayed(process_single_rdm)(rdm) for rdm in rdm_data
        )
    if return_array:
        return np.asarray(rsa_vals)
    else:
        return rsa_vals[0]


def rsa_array(
    X,
    rdm_model,
    patches=None,
    data_rdm_metric="correlation",
    data_rdm_params=dict(),
    rsa_metric="spearman",
    ignore_nan=False,
    y=None,
    n_folds=1,
    n_jobs=1,
    verbose=False,
):
    """Perform RSA on an array of data, possibly in a searchlight pattern.

    Parameters
    ----------
    X : ndarray, shape (n_items, n_series, n_times)
        An array containing the data.
    rdm_model : ndarray, shape (n, n) | (n * (n - 1) // 2,) | list of ndarray
        The model RDM, see :func:`compute_rdm`. For efficiency, you can give it in
        condensed form, meaning only the upper triangle of the matrix as a vector. See
        :func:`scipy.spatial.distance.squareform`. To perform RSA against multiple
        models at the same time, supply a list of model RDMs.

        Use :func:`compute_rdm` to compute RDMs.
    patches : generator of tuples | None
        Searchlight patches as generated by :class:`searchlight`. If ``None``, no
        searchlight is used. Defaults to ``None``.
    data_rdm_metric : str
        The metric to use to compute the data RDMs. This can be any metric supported by
        the scipy.distance.pdist function. Defaults to 'correlation'.
    data_rdm_params : dict
        Extra arguments for the distance metric used to compute the RDMs. Refer to
        :mod:`scipy.spatial.distance` for a list of all other metrics and their
        arguments. Defaults to an empty dictionary.
    rsa_metric : str
        The RSA metric to use to compare the RDMs. Valid options are:

        * 'spearman' for Spearman's correlation (the default)
        * 'pearson' for Pearson's correlation
        * 'kendall-tau-a' for Kendall's Tau (alpha variant)
        * 'partial' for partial Pearson correlations
        * 'partial-spearman' for partial Spearman correlations
        * 'regression' for linear regression weights

        Defaults to 'spearman'.
    ignore_nan : bool
        Whether to treat NaN's as missing values and ignore them when computing the
        distance metric. Defaults to ``False``.

        .. versionadded:: 0.8
    y : ndarray of int, shape (n_items,) | None
        (Deprecated) For each item, a number indicating the class to which the item
        belongs.  When ``None``, each item is assumed to belong to a different class.
        Defaults to ``None``.
    labels_rdm_model: list | None
        For each row in ``rdm_model``, a label that identifies the item to which it
        corresponds. This is used in combination with ``labels_X`` to align the data and
        model RDMs before comparing them. Each row should have a unique label. Labels
        may be of any python type that can be compared with ``==`` (int, float, string,
        tuple, etc). By default (``None``), the integers ``0:n_rows`` are used as
        labels.

        .. versionadded:: 0.10
    labels_X : list | None
        For each element in ``X`` (=the first dimension), a label that identifies the
        item to which it corresponds. This is used in combination with
        ``labels_rdm_model`` to align the data and model RDMs before comparing them.
        Multiple elements in ``X`` may correspond to the same item, in which case they
        should have the same label and will be averaged when computing the data RDM.
        Labels may be of any python type that can be compared with ``==`` (int, float,
        string, tuple, etc). By default (``None``), the integers ``0:len(X)`` are used
        as labels.

        .. versionadded:: 0.10
    n_folds : int | sklearn.model_selection.BaseCrollValidator | None
        Number of cross-validation folds to use when computing the distance metric.
        Folds are created based on the ``y`` parameter. Specify ``None`` to use the
        maximum number of folds possible, given the data. Alternatively, you can pass a
        Scikit-Learn cross validator object (e.g. ``sklearn.model_selection.KFold``) to
        assert fine-grained control over how folds are created.
        Defaults to 1 (no cross-validation).
    n_jobs : int
        The number of processes (=number of CPU cores) to use. Specify -1 to use all
        available cores. Defaults to 1.
    verbose : bool
        Whether to display a progress bar. In order for this to work, you need the tqdm
        python module installed. Defaults to False.

    Returns
    -------
    rsa_vals : ndarray, shape ([n_series,] [n_times,] [n_model_rdms])
        The RSA value for each searchlight patch. When ``spatial_radius`` is set to
        ``None``, there will only be no ``n_series`` dimension. When ``temporal_radius``
        is set to ``None``, there will be no time dimension. When multiple models have
        been supplied, the last dimension will contain RSA results for each model.

    See Also
    --------
    searchlight
    compute_rdm
    rdm_array

    """
    if patches is None:
        patches = searchlight(X.shape)  # One big searchlight patch

    # Create folds for cross-validated RDM metrics
    X = create_folds(X, y, n_folds)
    # The data is now folds x items x n_series x n_times

    if isinstance(rdm_model, list):
        rdm_model = [_ensure_condensed(rdm, "rdm_model") for rdm in rdm_model]
    else:
        rdm_model = [_ensure_condensed(rdm_model, "rdm_model")]

    if ignore_nan:
        masks = [~np.isnan(rdm) for rdm in rdm_model]
    else:
        masks = [slice(None)] * len(rdm_model)

    if verbose:
        from tqdm import tqdm

        shape = getattr(patches, "shape", (-1,))
        patches = tqdm(patches, unit="patch")
        try:
            setattr(patches, "shape", shape)
        except AttributeError:
            pass

    def rsa_single_patch(patch):
        """Compute RSA for a single searchlight patch."""
        if len(X) == 1:  # Check number of folds
            # No cross-validation
            rdm_data = compute_rdm(X[0][patch], data_rdm_metric, **data_rdm_params)
        else:
            # Use cross-validation
            rdm_data = compute_rdm_cv(
                X[(slice(None),) + patch], data_rdm_metric, **data_rdm_params
            )
        if ignore_nan:
            data_mask = ~np.isnan(rdm_data)
            patch_masks = [m & data_mask for m in masks]
        else:
            patch_masks = masks
        return _rsa_single_rdm(rdm_data, rdm_model, rsa_metric, patch_masks)

    # Call RSA multiple times in parallel for each searchlight patch
    data = Parallel(n_jobs=n_jobs)(
        delayed(rsa_single_patch)(patch) for patch in patches
    )

    # Figure out the desired dimensions of the resulting array
    dims = getattr(patches, "shape", (-1,))
    if len(rdm_model) > 1:
        dims = dims + (len(rdm_model),)

    return np.array(data).reshape(dims)
