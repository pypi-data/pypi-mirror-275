from furtheredge.abstracted_packages import furtheredge_numpy as np

payment_months = {
    1: [12],
    2: [6, 12],
    4: [3, 6, 9, 12],
    12: list(range(1, 13)),
}


def duration_calculation(merged_df, persistency_rate=1):
    """
    Perform duration calculation for the given DataFrame by applying various
    calculation functions and adding new columns with the results.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy and financial data.
        persistency_rate (float, optional): Rate of persistency to be applied. Default is 1.

    Returns:
        pandas.DataFrame: DataFrame with additional columns calculated based on input data.
    """
    # print("Duration calculation")

    merged_df["IND_PAY"] = _payment_month(merged_df)

    merged_df["IND_IF"] = _indicator_policy_if(merged_df)

    merged_df["PREM_DUR"] = _premium_duration(merged_df, persistency_rate)

    merged_df["FEE_AMT"] = _fees_amount(merged_df)

    merged_df["ACQ_LOAD"] = _acquisition_loading(merged_df)

    merged_df["PREM_ALL_AMT_DUR"] = _premium_allocation_amount_dur(merged_df)

    merged_df["QX_DEATH"] = _qx_death(merged_df)

    merged_df["QX_PTD"] = _qx_ptd(merged_df)

    merged_df["QX_PTD_ADDITIONAL"] = _qx_ptd_additional(merged_df)

    merged_df["QX_CRITICAL_ILLNESS_ADD"] = _qx_critical_illness_additional(
        merged_df
    )

    merged_df["QX_PPD"] = _qx_ppd(merged_df)

    merged_df["QX_ADB"] = _qx_adb(merged_df)

    merged_df["QX_WOP"] = _qx_wop(merged_df)

    merged_df["QX_CRITICAL_ILLNESS_ACC"] = _qx_critical_illness_accelerated(
        merged_df
    )
    return merged_df


def _payment_month(merged_df):
    """
    Calculate the payment indicator for each row in the DataFrame based on payment months.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing payment indicators for each row.
    """
    mp_pay_mode_dict = dict(zip(merged_df["MP_ID"], merged_df["PAY_MODE"]))

    months = merged_df["fin_mois"].dt.month

    def payment_indicator(row):
        mp_id = row["MP_ID"]
        current_pay_mode = mp_pay_mode_dict.get(mp_id)
        return (
            1
            if row["month"] in payment_months.get(current_pay_mode, [])
            else 0
        )

    merged_df["month"] = months
    merged_df["PAYMENT_INDICATOR"] = merged_df.apply(payment_indicator, axis=1)

    return merged_df["PAYMENT_INDICATOR"]


def _indicator_policy_if(merged_df):
    """
    Calculate the policy in-force indicator for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing in-force indicators for each row.
    """
    policy_term_m = merged_df["POLICY_TERM_M"]
    duration_if_m = merged_df["DURATIONIF_M"]
    month_index = merged_df["month_index"]
    indicator = (month_index <= (policy_term_m - duration_if_m)).astype(
        np.int64
    )
    return indicator


def _premium_duration(merged_df, persistency_rate=1):
    """
    Calculate the premium duration for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.
        persistency_rate (float, optional): Rate of persistency to be applied. Default is 1.

    Returns:
        pandas.Series: Series containing premium durations for each row.
    """

    return (
        merged_df["MODAL_PREM_AMT"]
        * merged_df["IND_PAY"]
        * merged_df["IND_IF"]
        * persistency_rate
    )


def _fees_amount(merged_df):
    """
    Calculate the fees amount for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing fees amounts for each row.
    """

    sa_death = merged_df["SA_COV1_AMT"]
    sa_loading_pm = merged_df["SA_LOADING_PM"]

    return sa_death * merged_df["IND_IF"] * ((sa_loading_pm / 1000) / 12)


def _acquisition_loading(merged_df):
    """
    Calculate the acquisition loading for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing acquisition loadings for each row.
    """

    return (
        merged_df["MODAL_PREM_AMT"]
        * merged_df["PREM_LOADING_PC"]
        * merged_df["IND_PAY"]
    )


def _premium_allocation_amount_dur(output):
    """
    Calculate the premium allocation amount duration for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing premium allocation amounts for each row.
    """

    return output["PREM_DUR"] - output["FEE_AMT"] - output["ACQ_LOAD"]


def _qx_death(merged_df):
    """
    Calculate the probability of death for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing probabilities of death for each row.
    """
    return (
        merged_df["COI_PC"]
        * ((merged_df["RATE_Death"] / 1000) / 12)
        * merged_df["IND_IF"]
        * (1 + merged_df["X_PREM_COV11_PC"])
    )


def _qx_ptd(merged_df):
    """
    Calculate the probability of total and permanent disability (TPD) for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing probabilities of TPD for each row.
    """
    cover_tpd_rate = merged_df["RATE_TPD Accelerator Any"]
    coi_pc = merged_df["COI_PC"]
    sa_cov2_amt = merged_df["SA_COV2_AMT"]
    sa_cov2_pc = sa_cov2_amt != 0

    return (
        coi_pc
        * ((cover_tpd_rate / 1000) / 12)
        * merged_df["IND_IF"]
        * sa_cov2_pc
    )


def _qx_ptd_additional(merged_df):
    """
    Calculate the probability of additional total and permanent disability (TPD) for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing probabilities of additional TPD for each row.
    """

    cover_tpd_add_rate = merged_df["RATE_TPD Accelerator Any"]
    coi_pc = merged_df["COI_PC"]
    sa_cov3_amt = merged_df["SA_COV3_AMT"]
    sa_cov3_pc = sa_cov3_amt != 0

    return (
        coi_pc
        * ((cover_tpd_add_rate / 1000) / 12)
        * merged_df["IND_IF"]
        * sa_cov3_pc
    )


def _qx_critical_illness_additional(merged_df):
    """
    Calculate the probability of additional critical illness for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing probabilities of additional critical illness for each row.
    """

    cover_critical_illness_add_rate = merged_df["RATE_CI Accelerator (Male)"]
    coi_pc = merged_df["COI_PC"]
    sa_cov4_pc = merged_df["SA_COV4_AMT"]

    return (
        coi_pc
        * ((cover_critical_illness_add_rate / 1000) / 12)
        * merged_df["IND_IF"]
        * sa_cov4_pc
    )


def _qx_ppd(merged_df):
    """
    Calculate the probability of partial and permanent disability (PPD) for each row in the DataFrame.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy data.

    Returns:
        pandas.Series: Series containing probabilities of PPD for each row.
    """

    cover_ppd_rate = merged_df["RATE_Accidental PPD"]
    coi_pc = merged_df["COI_PC"]
    sa_cov6_pc = merged_df["SA_COV6_AMT"]

    return (
        coi_pc
        * ((cover_ppd_rate / 1000) / 12)
        * merged_df["IND_IF"]
        * sa_cov6_pc
    )


def _qx_adb(merged_df):
    """
    Calculate the probability of accidental death benefit (ADB) for each row
    in the output DataFrame based on model points.

    Returns:
        pandas.Series: Series containing the probability of accidental death benefit (ADB)
        for each row in the output DataFrame.
    """

    cover_adb_rate = merged_df["RATE_Accidental Death"]
    coi_pc = merged_df["COI_PC"]
    sa_cov7_pc = merged_df["SA_COV7_AMT"]

    return (
        coi_pc
        * ((cover_adb_rate / 1000) / 12)
        * merged_df["IND_IF"]
        * sa_cov7_pc
    )


def _qx_wop(merged_df):
    """
    Calculate the probability of waiver of premium (WOP) for each row
    in the output DataFrame based on model points.

    Returns:
        pandas.Series: Series containing the probability of waiver of premium (WOP)
        for each row in the output DataFrame.
    """

    wop_rate = merged_df["RATE"]
    coi_pc = merged_df["COI_PC"]
    sa_cov8_pc = merged_df["SA_COV8_AMT"]

    return coi_pc * ((wop_rate / 1000) / 12) * merged_df["IND_IF"] * sa_cov8_pc


def _qx_critical_illness_accelerated(merged_df):
    """
    Calculate the probability of accelerated critical illness for each row
    in the output DataFrame based on model points.

    Returns:
        pandas.Series: Series containing the probability of accelerated critical illness
        for each row in the output DataFrame.
    """

    cover_critical_illness_acc_rate = merged_df["RATE_CI Accelerator (Male)"]
    coi_pc = merged_df["COI_PC"]
    sa_cov10_pc = merged_df["SA_COV10_AMT"]

    return (
        coi_pc
        * ((cover_critical_illness_acc_rate / 1000) / 12)
        * merged_df["IND_IF"]
        * sa_cov10_pc
    )
