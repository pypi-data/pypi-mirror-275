from furtheredge.abstracted_packages import furtheredge_pandas as pd


def lowercase_string_columns(df):
    """
    Transform all string columns in a DataFrame to lowercase.

    Args:
    - df (DataFrame): Input DataFrame.

    Returns:
    - DataFrame: DataFrame with string columns transformed to lowercase.
    """
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].str.lower()

    return df


def initialize_output_dataframe(
    number_of_model_points,
    duration_month,
    starting_projection_date,
    start_index,
):
    """
    Initialize the output DataFrame with model points and projection duration.

    Args:
    - number_of_model_points (int): Number of model points.
    - duration_month (int): Duration of projection in months.
    - starting_projection_date (str): Starting date of projection.

    Returns:
    - DataFrame: Initialized DataFrame with model points and projection duration.

    This function initializes the output DataFrame with model points and projection duration.
    It creates a DataFrame containing model point IDs, month indices, and month-end dates
    for the specified duration starting from the given projection start date.
    """
    dfs = []
    fin_mois = pd.date_range(
        start=starting_projection_date, periods=duration_month, freq="ME"
    )
    for i in range(start_index + 1, start_index + number_of_model_points + 1):
        df = pd.DataFrame(
            {
                "MP_ID": i,
                "month_index": range(duration_month),
                "fin_mois": fin_mois,
            }
        )
        dfs.append(df)
    result_df = pd.concat(dfs, ignore_index=True)
    return result_df[["MP_ID", "month_index", "fin_mois"]]


def merge_all_dfs_police(
    model_points,
    ri_rates,
    wop_rates,
    tech_assumptions,
    product,
    projection_date,
    projection_points,
):
    first_index = model_points.index[0]

    output = initialize_output_dataframe(
        len(model_points), projection_points, projection_date, first_index
    )

    # Merging the output table with the modelpoint table
    output = pd.merge(output, model_points, on="MP_ID", how="left")

    # Merging the output table with the product table
    output = pd.merge(
        output,
        product,
        on=["PRODUCT_ID", "PRODUCT_NAME", "PRODUCT_TYPE"],
        how="left",
    )

    # Merging the output table with the Tech Assumptions
    output["PROJECTION_YR"] = (
        ((output["DURATIONIF_M"] + output["month_index"]) // 12) + 1
    ).clip(upper=11)

    output = pd.merge(
        output, tech_assumptions, on=["TECH_ASSUMPTION_ID", "PROJECTION_YR"]
    )

    # Merging the output table with the WOP_RATES Table
    output["AGE"] = output["AGE_AT_ENTRY"] + (
        (output["DURATIONIF_M"] + output["month_index"]) // 12
    )

    output = pd.merge(
        output,
        wop_rates,
        left_on=["WOP_RATES_ID", "AGE", "PROJECTION_YR"],
        right_on=["WOP_RATES_ID", "AGE", "PROJ_YR"],
    )

    # Merging the output table with the RI_RATES Table
    ri_rates_pivot = ri_rates.pivot(
        index=["RI_RATES_ID", "AGE"], columns="COVER", values="RATE"
    )

    output = pd.merge(
        output,
        ri_rates_pivot,
        left_on=["RI_RATES_ID", "AGE"],
        right_index=True,
        how="left",
    )

    output.rename(
        columns={col: f"RATE_{col}" for col in ri_rates_pivot.columns},
        inplace=True,
    )

    return output
