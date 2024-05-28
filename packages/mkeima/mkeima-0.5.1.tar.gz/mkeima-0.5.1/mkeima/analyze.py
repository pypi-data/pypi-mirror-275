"""This module provides functions for analyzing FACS data.

The following functions are available:

- `calculate_mkeima_score`: Adds "low pH mkeima" to "high pH mkeima" scores. mKeima
    scores are log ratios of low pH to high pH mKeima signals, normalized to a reference
    sample by calculating z-scores using the median and standard deviation of the
    reference sample.
- `summarize`: Calculates summary statistics (mean, median, std, and number  of cells).
- `summarize_outliers`: Calculates the amount of outliers for each condition and
    replicate. Outliers are defined as events with a value above the a certain
    percentile (by default 98.5%) of the reference population.
"""
from typing import Optional

import pandas as pd
import numpy as np


def calculate_mkeima_score(
    data: pd.DataFrame,
    high_ph: str,
    low_ph: str,
    reference: str,
    group_by: Optional[str] = None,
    log_transform: bool = False,
) -> None:
    """Adds normalized "low pH mkeima" to "high pH mkeima" scores.

    Mkeima scores are normalized log ratios of low pH to high pH mKeima signals and
    calculated as follows. Low pH mKeima signals are divided by high pH mKeima signals
    and the ratios are log transformed. Log ratios are then normalized to the reference
    condition by subtracting the median of the of the reference population and then
    dividing by the standard deviation of the reference population. Normalized log
    ratios are added to the dataframe column "mkeima score".

    Args:
        data: Dataframe containing FACS data.
        high_ph: Column corresponding to the high pH mKeima channel.
        low_ph: Column corresponding to the low pH mKeima channel.
        reference: Reference condition used to normalize ratios of low pH to high pH
            ratios. Must correspond to a value in data["Condition"].
        group_by: Optional, if specified the dataframe is grouped by unique values of
            this column and each group is normalized independently to the reference
            condition.
        log_transform: Default False. If True low pH and high pH values are log
            transformed before calculating mkeima scores. Only use this option when the
            reported FACS intensities are not already in log-space. It is recommended to
            export channel values from FlowJo, which are already log transformed.
    """
    if reference not in data["Condition"].unique():
        raise KeyError(
            f'The reference condition "{reference}" is not '
            f'present in data["Condition"]!'
        )

    if log_transform:
        data["mkeima score"] = np.log(data[low_ph]) - np.log(data[high_ph])
    else:
        data["mkeima score"] = data[low_ph] - data[high_ph]

    group_masks = []
    if group_by is not None:
        for group_name in data[group_by].unique():
            group_masks.append(data[group_by] == group_name)
    else:
        group_masks.append(np.ones(data.shape[0], dtype=bool))

    for group_mask in group_masks:
        group_data = data.loc[group_mask]

        norm_data = group_data.loc[(group_data["Condition"] == reference)]
        norm_median = np.median(norm_data["mkeima score"])
        norm_std = np.std(norm_data["mkeima score"])

        mkeima_scores = (group_data["mkeima score"] - norm_median) / norm_std
        mkeima_scores = mkeima_scores
        data.loc[group_mask, "mkeima score"] = mkeima_scores


def summarize(
    data: pd.DataFrame,
    group_by: list[str] = ["Condition", "Replicate"],
    on: str = "mkeima score",
) -> pd.DataFrame:
    """Calculates summary statistics.

    Total number of cells (i.e. FACS events), mean, standard deviation, median.

    Args:
        data: Dataframe used for summarizing.
        group_by: Default ["Condition", "Replicate"]. List of dataframe columns that
            will be used for grouping data before summarizing each group individually.
            Should include all columns that are necessary to distinguish each unique
            sample.
        on: Default "mkeima score". Specifies column that will be used for summarizing.

    Returns:
        A dataframe containing the columns used for grouping, as well as "Median",
        "Mean", "Std", and "Total cells".
    """
    results = (
        data.groupby(by=group_by)
        .agg(
            Median=(on, np.median),
            Mean=(on, np.mean),
            Std=(on, np.std),
            Total_cells=(on, "size"),
        )
        .reset_index()
    )
    results.rename(columns={"Total_cells": "Total cells"}, inplace=True)
    return results


def summarize_outliers(
    data: pd.DataFrame,
    reference: str,
    on: str = "mkeima score",
    reference_percentile: float = 98.5,
    group_by: Optional[list] = None,
) -> pd.DataFrame:
    """Calculates the amount of outliers for each condition and replicate.

    The threshold for outliers is defined as the 98.5 percentile of the mkeima score
    distribution from the reference condition. Entries in the dataframe are grouped
    according to unique values in the "Condition" and "Replicate" columns, and for each
    group the number and relative amount of outliers is calculated.

    Args:
        data: Dataframe used for summarizing. Must contain the columns "Condition" and
        "Replicate", as well as columns specified by the 'on' and 'group_by' arguments.
        reference: Reference condition that is used for calculating an outlier
            threshold. Must correspond to a value in data["Condition"].
        on: Default "mkeima score". Specifies column that will be used for calculation
            of outliers.
        reference_percentile: Percentile of the reference condition population that is
            used to calculate the outlier threshold.
        group_by: Optional, list of dataframe columns. If specified, the dataframe is
            first grouped by unique values of these columns and the outlier threshold
            and outliers are calculated for each group separately.

    Returns:
        A dataframe containing the columns "Condition", "Replicate", "Total cells",
        "Outliers", "Outliers [%]", and the columns specified by the 'group_by'
        argument.
    """
    default_grouping = ["Condition", "Replicate"]
    if group_by is not None:
        group_by = [by for by in group_by if by not in default_grouping]
        if not group_by:
            group_by = None

    if group_by is None:
        grouping = [(None, data)]
    else:
        grouping = data.groupby(group_by)

    group_results = []
    for group_name, group_data in grouping:
        reference_mask = group_data["Condition"] == reference
        reference_scores = group_data.loc[reference_mask, on]
        cutoff_uppers = np.percentile(reference_scores, reference_percentile)

        results = (
            group_data.groupby(by=default_grouping)
            .agg(
                Total_cells=(on, "size"),
                Outliers=(on, lambda x: (x >= cutoff_uppers).sum()),
            )
            .reset_index()
        )
        results["Outliers [%]"] = (results["Outliers"] / results["Total_cells"]) * 100
        results.rename(columns={"Total_cells": "Total cells"}, inplace=True)

        # Add columns from the user specified grouping
        if group_name is not None:
            if isinstance(group_name, str):
                group_name = (group_name,)
            for column_value, column in zip(group_name, group_by):
                results[column] = column_value
        group_results.append(results)
    results_table = pd.concat(group_results, ignore_index=True)
    return results_table
