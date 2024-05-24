from furtheredge.abstracted_packages import furtheredge_numpy as np
from furtheredge.abstracted_packages import furtheredge_pandas as pd


def reserve_calculation(merged_df):
    """
    Perform reserve calculations on the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data,
            including columns necessary for reserve calculations.

    Returns:
        pandas.DataFrame: DataFrame with additional columns for reserve calculations.
    """
    # model_points, output, tech_assumptions, product
    # print("Reserve calculation")

    merged_df["PREM_ALL_AMT_RES"] = _premium_allocation_amount_res(merged_df)

    merged_df["SAR_DEATH1"] = _sar_death1(merged_df)

    merged_df["SAR_DEATH2"] = _sar_death2(merged_df)

    merged_df["SAR_DEATH"] = _sar_death(merged_df)

    merged_df["SAR_OR"] = _sar_death(merged_df)

    merged_df["SAR_ADB2"] = _sar_adb2(merged_df)

    merged_df["SAR_ADB"] = _sar_adb(merged_df)

    merged_df["COI_DEATH"] = _coi_death(merged_df)

    merged_df["COI_OTHER_RIDERS"] = _coi_other_riders(merged_df)

    merged_df["COI_ADB"] = _coi_adb(merged_df)

    merged_df["FUND_VALUE"] = _fund_value(merged_df)

    merged_df["FMF"] = _fixed_management_fees(merged_df)

    merged_df["AV_FUND_VALUE"] = _av_fund_value(merged_df)

    merged_df["INTEREST"] = _interest(merged_df)
    return merged_df


def _premium_allocation_amount_res(merged_df):
    """
    Calculate the premium allocation amount for reserves.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing the premium allocation amount for reserves.
    """
    return merged_df["PREM_ALL_AMT_DUR"]


def _sar_death1(merged_df):
    """
    Calculate SAR Death 1.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing SAR Death 1.
    """

    merged_df = merged_df.copy()

    annual_int_rate = merged_df["INT_RATE"]
    monthly_int_rate = (1 + annual_int_rate) ** (1 / 12) - 1
    discount_factor = 1 / (1 + monthly_int_rate) ** (
        merged_df["month_index"] + 1
    )

    merged_df["produit"] = merged_df["PREM_ALL_AMT_RES"] * discount_factor
    merged_df = merged_df.iloc[::-1]
    grouped_data = merged_df.groupby("MP_ID")
    merged_df["van"] = grouped_data["produit"].cumsum()
    merged_df = merged_df.iloc[::-1]
    output_temp = pd.DataFrame()
    output_temp["shifted_col"] = (
        merged_df.groupby(["MP_ID"])["van"].shift(-1).fillna(0)
    )

    return output_temp["shifted_col"] / discount_factor


def _sar_death2(merged_df):
    """
    Calculate SAR Death 2.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing SAR Death 2.
    """
    sa_cov1_amt = merged_df["SA_COV1_AMT"]
    cash_value_fund1 = merged_df["CASH_VAL_FUND1"]
    merged_df["sar_death2"] = (
        sa_cov1_amt - cash_value_fund1 - merged_df["PREM_ALL_AMT_RES"]
    )
    merged_df.loc[merged_df["sar_death2"] < 0, "sar_death2"] = 0
    return merged_df["sar_death2"] * merged_df["IND_IF"]


def _sar_death(merged_df):
    """
    Determine the SAR Death based on product type.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing SAR Death.
    """
    merged_df["code_plan"] = merged_df["PRODUCT_TYPE"]

    return np.where(
        merged_df["code_plan"] == "Education",
        merged_df["SAR_DEATH1"],
        merged_df["SAR_DEATH2"],
    )


def _sar_adb2(merged_df):
    """
    Calculate SAR ADB 2.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing SAR ADB 2.
    """
    sa_cov7_amt = merged_df["SA_COV7_AMT"]
    cash_value_fund1 = merged_df["CASH_VAL_FUND1"]
    merged_df["sar_adb2"] = (
        sa_cov7_amt - cash_value_fund1 - merged_df["PREM_ALL_AMT_RES"]
    )
    merged_df.loc[merged_df["sar_adb2"] < 0, "sar_adb2"] = 0
    return merged_df["sar_adb2"] * merged_df["IND_IF"]


def _sar_adb(merged_df):
    """
    Determine the SAR ADB based on product ID.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing SAR ADB.
    """
    merged_df["product_id"] = merged_df["PRODUCT_ID"]

    sar_death_affected_values = [1, 2, 3]

    merged_df.loc[
        merged_df["product_id"].isin(sar_death_affected_values), "sar_adb"
    ] = merged_df["SAR_DEATH1"]

    adb2_affected_values = [4, 5, 6, 7]

    merged_df.loc[
        merged_df["product_id"].isin(adb2_affected_values), "sar_adb"
    ] = merged_df["SAR_ADB2"]

    return merged_df["sar_adb"]


def _coi_death(merged_df):
    """
    Calculate Cost of Insurance (COI) for death.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing COI for death.
    """
    return merged_df["SAR_DEATH"] * merged_df["QX_DEATH"]


def _coi_other_riders(merged_df):
    """
    Calculate Cost of Insurance (COI) for other riders.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing COI for other riders.
    """
    return merged_df["SAR_DEATH"] * (
        merged_df["QX_PTD"]
        + merged_df["QX_PTD_ADDITIONAL"]
        + merged_df["QX_CRITICAL_ILLNESS_ADD"]
        + merged_df["QX_PPD"]
        + merged_df["QX_WOP"]
        + merged_df["QX_CRITICAL_ILLNESS_ACC"]
    )


def _coi_adb(merged_df):
    """
    Calculate Cost of Insurance (COI) for ADB.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing COI for ADB.
    """
    return merged_df["SAR_DEATH"] * merged_df["QX_ADB"]


def _fund_value(merged_df):
    """
    Calculate fund value.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing fund values.
    """

    def calculate_fund_value(group):
        fund_values = []
        prev_fund_value = 0
        for index, row in group.iterrows():
            if row["month_index"] == 0:
                fund_value = (
                    row["PREM_ALL_AMT_RES"]
                    - row["COI_DEATH"]
                    - row["COI_OTHER_RIDERS"]
                    + row["CASH_VAL_FUND1"]
                ) * row["IND_IF"]
            else:
                fund_value = (
                    row["PREM_ALL_AMT_RES"]
                    - row["COI_DEATH"]
                    - row["COI_OTHER_RIDERS"]
                    + prev_fund_value
                ) * row["IND_IF"]
            fund_values.append(fund_value)
            prev_fund_value = fund_value
        group["FUND_VALUE"] = fund_values
        return group

    output_result = (
        merged_df.groupby("MP_ID")
        .apply(calculate_fund_value, include_groups=False)
        .reset_index(drop=True)
    )
    return output_result["FUND_VALUE"]


def _fixed_management_fees(merged_df):
    """
    Calculate fixed management fees.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing fixed management fees.
    """
    fmf_pc = merged_df["FMF_PC"]

    return (fmf_pc * merged_df["FUND_VALUE"]) / 12


def _av_fund_value(merged_df):
    """
    Calculate average fund value.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing average fund value.
    """
    mgr_pc = merged_df["MGR_PC"]

    return (merged_df["FUND_VALUE"] - merged_df["FMF"]) * (
        (1 + mgr_pc) ** (1 / 12)
    )


def _interest(merged_df):
    """
    Calculate interest.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data.

    Returns:
        pandas.Series: Series containing interest values.
    """
    return merged_df["AV_FUND_VALUE"] - merged_df["FUND_VALUE"]
