from furtheredge.modules.universal_life.sub_modules.reserve import _sar_death1
from furtheredge.abstracted_packages import furtheredge_pandas as pd
from furtheredge.abstracted_packages import furtheredge_numpy as np
from furtheredge.modules.universal_life import tools


def prospective_calculation(merged_df):
    """
    Perform prospective calculations for the given DataFrame by applying various
    calculation functions and adding new columns with the results.

    Args:
        merged_df (pandas.DataFrame): Input DataFrame containing policy and financial data.

    Returns:
        pandas.DataFrame: DataFrame with additional columns calculated based on input data.
    """
    # model_points, output, tech_assumptions, product
    # print("Prospective calculation")

    merged_df["PREM_PROS"] = _prem_pros(merged_df)
    merged_df["COMISSION_AMT"] = commission_amt(merged_df)
    merged_df["DEATH_CLAIMS"] = death_claim(merged_df)
    merged_df["SURR_CLAIM"] = surrender_claims(merged_df)

    merged_df["MATURITY_CLAIM"] = maturity_claims(merged_df)

    merged_df["MAIN_EXPENS"] = maintenance_expenses(merged_df)

    merged_df["CEDED_SA"] = ceded_sum_assured(merged_df)

    merged_df["CESSION_RATE"] = cession_rate(merged_df)

    merged_df["PREM_REINS"] = premium_paid_to_reinsurer(merged_df)
    merged_df["COMISS_REINS"] = commission_received_from_reinsurer(merged_df)
    merged_df["CLAIM_REINS"] = claims_paid_by_reinsurer(merged_df)
    merged_df["REINS_PROF_SHAR"] = reinsurance_profit_sharing(merged_df)

    merged_df["APV_PREM"] = adjusted_present_value_premium(merged_df)

    merged_df["APV_DEATH"] = adjusted_present_value_death(merged_df)

    merged_df["APV_SURR"] = adjusted_present_value_surr(merged_df)

    merged_df["APV_MATURITY"] = adjusted_present_value_maturity(merged_df)

    merged_df["APV_EXPENSES"] = adjusted_present_value_expenses(merged_df)
    return merged_df


def _prem_pros(merged_df):
    """
    Calculate premium prospects for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for premium prospect calculation.

    Returns:
        pandas.Series: Series containing the premium prospects for each row
        in the merged_df DataFrame.
    """

    return merged_df["PREM_DUR"] * merged_df["TPX"]


def commission_amt(merged_df):
    """
    Calculate the commission amount for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for commission calculation.

    Returns:
        pandas.Series: Series containing the commission amount for each row
        in the merged_df DataFrame.
    """

    commissions_pc = merged_df["COMMISSIONS_PC"]
    return merged_df["PREM_PROS"] * commissions_pc


def death_claim(merged_df):
    """
    Calculate death claims for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for death claim calculation.

    Returns:
        pandas.Series: Series containing the death claims for each row
        in the merged_df DataFrame.
    """
    cover_1_survival_probability = (1 - merged_df["MORTALITY_RATE_DEATH"]) ** (
        1 / 12
    )
    or_survival_probability = (1 - merged_df["MORTALITY_RATE_OR"]) ** (1 / 12)
    cover_7_survival_probability = (1 - merged_df["MORTALITY_RATE_ADB"]) ** (
        1 / 12
    )
    tpx = merged_df["TPX"]
    if_ind = merged_df["IND_IF"]
    sar_death1 = _sar_death1(merged_df)
    prm_allocation_amount_av_fund = (
        merged_df["AV_FUND_VALUE"] + merged_df["PREM_ALL_AMT_RES"]
    )
    return (
        prm_allocation_amount_av_fund * (1 - cover_1_survival_probability)
        + prm_allocation_amount_av_fund * (1 - or_survival_probability)
    ) * tpx * if_ind + (
        sar_death1 * (1 - cover_1_survival_probability)
        + (1 - or_survival_probability) * (1 - cover_7_survival_probability)
    ) * tpx * if_ind


def surrender_claims(merged_df):
    """
    Calculate surrender claims for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for surrender claim calculation.

    Returns:
        pandas.Series: Series containing the surrender claims for each row
        in the merged_df DataFrame.
    """

    death_mortality_rate = merged_df["MORTALITY_RATE_DEATH"]
    or_mortality_rate = merged_df["MORTALITY_RATE_OR"]
    abd_mortality_rate = merged_df["MORTALITY_RATE_ADB"]
    if_ind = merged_df["IND_IF"]
    tpx = merged_df["TPX"]
    surrender_charge = merged_df["SURRENDER_CHARGE_FIXED_AMT"]
    av_fund = merged_df["AV_FUND_VALUE"]
    lapse_rate = merged_df["LAPSE_RATE_PC"]
    unclaimed_policies = (1 - lapse_rate) ** (1 / 12)

    surr_claim = (
        av_fund
        * (1 - unclaimed_policies)
        * tpx
        * if_ind
        * (1 - surrender_charge)
        * (1 - death_mortality_rate - or_mortality_rate - abd_mortality_rate)
        ** (1 / 12)
    )
    return surr_claim


def maturity_claims(merged_df):
    """
    Calculate maturity claims for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for maturity claim calculation.

    Returns:
        pandas.Series: Series containing the maturity claims for each row
        in the merged_df DataFrame.
    """
    duration_if = merged_df["DURATIONIF_M"]
    projected_m = duration_if + merged_df["month_index"]
    policy_term_m = merged_df["POLICY_TERM_M"]
    av_fund = merged_df["AV_FUND_VALUE"]
    conditional_value = pd.Series(0, index=merged_df.index)
    conditional_value[projected_m == policy_term_m] = av_fund.astype(
        conditional_value.dtype
    )
    tpx = merged_df["TPX"]
    maturity_claim = conditional_value * tpx
    return maturity_claim


def maintenance_expenses(merged_df):
    """
    Calculate maintenance expenses for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for maintenance expense calculation.

    Returns:
        pandas.Series: Series containing the maintenance expenses for each row
        in the merged_df DataFrame.
    """
    tpx = merged_df["TPX"]
    if_ind = merged_df["IND_IF"]
    prem_pros = merged_df["PREM_PROS"]
    fixed_loading_amt = merged_df["FIXED_LOADING_AMT"]

    inflation_pc = merged_df["INFLATION_PC"]

    variable_loading_pc = merged_df["VARIABLE_LOADING_PC"]

    duration = 1
    main_expens = (
        tpx
        * fixed_loading_amt
        / 12
        * if_ind
        * (1 + inflation_pc) ** (duration - 1)
        + variable_loading_pc * prem_pros
    ) * if_ind
    return main_expens


def ceded_sum_assured(merged_df):
    """
    Calculate ceded sum assured for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for ceded sum assured calculation.

    Returns:
        pandas.Series: Series containing the ceded sum assured for each row
        in the merged_df DataFrame.
    """

    sa_cov1_amt = merged_df["SA_COV1_AMT"]

    ret_cov1_amt = merged_df["RET_COV1_AMT"]
    ceded_sa = np.maximum(sa_cov1_amt - ret_cov1_amt, 0)
    return ceded_sa


def cession_rate(merged_df):
    """
    Calculate cession rate for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for cession rate calculation.

    Returns:
        pandas.Series: Series containing the cession rate for each row
        in the merged_df DataFrame.
    """

    ceded_sa = merged_df["CEDED_SA"]
    sa_cov1_amt = merged_df["SA_COV1_AMT"]
    cess_rate = ceded_sa / sa_cov1_amt
    return cess_rate


def premium_paid_to_reinsurer(merged_df):
    """
    Calculate premium paid to reinsurer for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for premium paid to reinsurer calculation.

    Returns:
        pandas.Series: Series containing the premium paid to reinsurer for each row
        in the merged_df DataFrame.
    """
    cess_rate = merged_df["CESSION_RATE"]

    coi_death = merged_df["COI_DEATH"]
    coi_or = merged_df["COI_OTHER_RIDERS"]
    coi_adb = merged_df["COI_ADB"]
    tpx = merged_df["TPX"]
    coi = merged_df["COI_PC"]
    prem_reins = cess_rate * (coi_death + coi_or + coi_adb) * tpx / coi

    return prem_reins


def commission_received_from_reinsurer(merged_df):
    """
    Calculate commission received from reinsurer for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for commission received from reinsurer calculation.

    Returns:
        pandas.Series: Series containing the commission received from reinsurer for each row
        in the merged_df DataFrame.
    """
    ri_commission_pc = merged_df["RI_COMMISSION_PC"]
    prem_reins = merged_df["PREM_REINS"]
    projection_yr = (merged_df["month_index"] // 12) + 1

    commission_year_1 = -ri_commission_pc * prem_reins
    condition_year_1 = projection_yr == 1
    comiss_reins = commission_year_1 * prem_reins * condition_year_1
    return comiss_reins


def claims_paid_by_reinsurer(merged_df):
    """
    Calculate claims paid by reinsurer for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for claims paid by reinsurer calculation.

    Returns:
        pandas.Series: Series containing the claims paid by reinsurer for each row
        in the merged_df DataFrame.
    """

    cess_rate = merged_df["CESSION_RATE"]
    sar_death1 = merged_df["SAR_DEATH"]
    sar_or = merged_df["SAR_OR"]
    sar_adb = merged_df["SAR_ADB"]

    death_survival_proba = (1 - merged_df["MORTALITY_RATE_DEATH"]) ** (1 / 12)
    or_survival_proba = (1 - merged_df["MORTALITY_RATE_OR"]) ** (1 / 12)
    adb_survival_proba = (1 - merged_df["MORTALITY_RATE_ADB"]) ** (1 / 12)

    tpx = merged_df["TPX"]
    if_ind = merged_df["IND_IF"]
    emf = merged_df["EMF"]
    claim_reins = (
        cess_rate
        * (
            sar_death1 * (1 - death_survival_proba)
            + sar_or * (1 - or_survival_proba)
            + sar_adb * (1 - adb_survival_proba)
        )
        * tpx
        * if_ind
    ) / emf
    return claim_reins


def reinsurance_profit_sharing(merged_df):
    """
    Calculate reinsurance profit sharing for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for reinsurance profit sharing calculation.

    Returns:
        pandas.Series: Series containing the reinsurance profit sharing for each row
        in the merged_df DataFrame.
    """
    prem_reins = merged_df["PREM_REINS"]
    comiss_reins = merged_df["COMISS_REINS"]
    claim_reins = merged_df["CLAIM_REINS"]
    reins_prof_shar = np.maximum(
        0.5 * (1 - 0.15) * (-prem_reins) * comiss_reins * claim_reins, 0
    )
    return reins_prof_shar


def adjusted_present_value_premium(merged_df):
    """
    Calculate adjusted present value of premiums for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for adjusted present value premium calculation.

    Returns:
        pandas.Series: Series containing the adjusted present value of premiums for each row
        in the merged_df DataFrame.
    """
    apv_prem = tools.npv(merged_df, "PREM_PROS")

    return apv_prem


def adjusted_present_value_death(merged_df):
    """
    Calculate adjusted present value of death claims for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for adjusted present value death calculation.

    Returns:
        pandas.Series: Series containing the adjusted present value of death claims for each row
        in the merged_df DataFrame.
    """
    apv_death = tools.npv(merged_df, "DEATH_CLAIMS")

    return apv_death


def adjusted_present_value_surr(merged_df):
    """
    Calculate adjusted present value of surrender claims for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for adjusted present value surrender calculation.

    Returns:
        pandas.Series: Series containing the adjusted present value of surrender claims for each row
        in the merged_df DataFrame.
    """

    apv_surr = tools.npv(merged_df, "SURR_CLAIM")

    return apv_surr


def adjusted_present_value_maturity(merged_df):
    """
    Calculate adjusted present value of maturity claims for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for adjusted present value maturity calculation.

    Returns:
        pandas.Series: Series containing the adjusted present value of maturity claims for each row
        in the merged_df DataFrame.
    """
    apv_maturity = tools.npv(merged_df, "MATURITY_CLAIM")

    return apv_maturity


def adjusted_present_value_expenses(merged_df):
    """
    Calculate adjusted present value of expenses for each row in the merged_df DataFrame.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged_df data, including
            columns necessary for adjusted present value expense calculation.

    Returns:
        pandas.Series: Series containing the adjusted present value of expenses for each row
        in the merged_df DataFrame.
    """
    apv_expenses = tools.npv(merged_df, "PREM_REINS")

    return apv_expenses
