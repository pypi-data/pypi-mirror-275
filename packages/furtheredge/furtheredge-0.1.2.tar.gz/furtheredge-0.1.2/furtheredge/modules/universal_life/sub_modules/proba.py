from furtheredge.abstracted_packages import furtheredge_numpy as np


def proba_calculation(merged_df):
    """
    Perform probability calculations for the given DataFrame by applying various
    calculation functions and adding new columns with the results.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy and financial data.

    Returns:
        pandas.DataFrame: DataFrame with additional columns calculated based on input data.
    """
    # model_points, output, tech_assumptions, ri_rates, product
    # print("Proba calculation")

    merged_df["MORTALITY_RATE_DEATH"] = _mortality_rate_death(merged_df)
    merged_df["MORTALITY_RATE_OR"] = _mortality_rate_or(merged_df)
    merged_df["MORTALITY_RATE_ADB"] = _mortality_rate_adb(merged_df)
    merged_df["TPX"] = tpx(merged_df)
    return merged_df


def _mortality_rate_death(merged_df):
    """
    Calculate the mortality rate due to death for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing mortality rates due to death for each row.
    """
    cover_death_rate = merged_df["RATE_Death"]

    return (
        merged_df["EMF"]
        * (cover_death_rate / 1000)
        * merged_df["IND_IF"]
        * (1 + merged_df["X_PREM_COV11_PC"])
    )


def _mortality_rate_or(merged_df):
    """
    Calculate the overall mortality rate for each row in the DataFrame by summing up
    various other rates.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing overall mortality rates for each row.
    """
    return (
        merged_df["QX_PTD"]
        + merged_df["QX_PTD_ADDITIONAL"]
        + merged_df["QX_CRITICAL_ILLNESS_ADD"]
        + merged_df["QX_PPD"]
        + merged_df["QX_WOP"]
        + merged_df["QX_CRITICAL_ILLNESS_ACC"]
    ) * 12


def _mortality_rate_adb(merged_df):
    """
    Calculate the mortality rate due to accidental death benefit (ADB) for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing mortality rates due to ADB for each row.
    """
    cover_adb_rate = merged_df["RATE_CI Accelerator (Female)"]

    return (cover_adb_rate / 1000) * merged_df["IND_IF"]


def tpx(merged_df):
    """
    Calculate the survival probability (tpx) for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing survival probabilities for each row.
    """
    death_survival_probability = (1 - merged_df["MORTALITY_RATE_DEATH"]) ** (
        1 / 12
    )
    or_survival_probability = (1 - merged_df["MORTALITY_RATE_OR"]) ** (1 / 12)
    adb_survival_probability = (1 - merged_df["MORTALITY_RATE_ADB"]) ** (
        1 / 12
    )
    lapse_rate = merged_df["LAPSE_RATE_PC"]
    unclaimed_policies = (1 - lapse_rate) ** (1 / 12)
    merged_df["SURVIVAL_PROBABILITY"] = (
        death_survival_probability
        * or_survival_probability
        * adb_survival_probability
        * unclaimed_policies
    )

    tpx_values = np.zeros(len(merged_df))
    prev_tpx_value = 0
    for mp_id, group in merged_df.groupby("MP_ID"):
        mask = group["month_index"] == 0
        tpx_values[group.index[mask]] = 1
        indices = group.index[~mask]
        tpx_values[indices] = (
            prev_tpx_value * group.loc[indices, "SURVIVAL_PROBABILITY"]
        )
        prev_tpx_value = tpx_values[indices[-1]]

    merged_df["TPX"] = tpx_values
    return merged_df["TPX"]
