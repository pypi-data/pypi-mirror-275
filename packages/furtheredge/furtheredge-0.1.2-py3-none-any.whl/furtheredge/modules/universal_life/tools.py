from furtheredge.abstracted_packages import furtheredge_pandas as pd


def age_projection_per_model_point(model_points, output):
    """
    Calculate the projected age for each model point based on the provided output data.

    Args:
        model_points (pandas.DataFrame): A DataFrame containing model points data,
            including columns 'MP_ID', 'DURATIONIF_M', and 'AGE_AT_ENTRY'.
        output (pandas.DataFrame): A DataFrame containing output data, including
            column 'MP_ID' to map model points, and 'month_index' for projection.

    Returns:
        pandas.Series: A Series containing the projected age for each model point.
    """
    duration_if = output["MP_ID"].map(
        model_points.set_index("MP_ID")["DURATIONIF_M"]
    )
    age_at_entry = output["MP_ID"].map(
        model_points.set_index("MP_ID")["AGE_AT_ENTRY"]
    )
    return (
        age_at_entry + ((duration_if + output["month_index"]) // 12)
    ).rename("Age")


def tech_assumptions_projection_output(
    model_points, output, tech_assumptions, product, col_name
):
    """
    Perform projection based on technical assumptions and generate output.

    Args:
        model_points (pandas.DataFrame): DataFrame containing model points data,
            including the column 'MP_ID'.
        output (pandas.DataFrame): DataFrame containing output data, including
            columns 'MP_ID' and 'month_index'.
        tech_assumptions (pandas.DataFrame): DataFrame containing technical assumptions,
            including columns 'TECH_ASSUMPTION_ID' and 'PROJECTION_YR'.
        product (pandas.DataFrame): DataFrame containing product data, including
            columns 'PRODUCT_ID' and 'TECH_ASSUMPTION_ID'.
        col_name (str): Name of the column to be returned from the merged DataFrame.

    Returns:
        pandas.Series: Series containing the projected output based on technical assumptions.
    """
    duration_if = output["MP_ID"].map(
        model_points.set_index("MP_ID")["DURATIONIF_M"]
    )
    projection_yr = (
        (((duration_if + output["month_index"]) // 12) + 1)
        .clip(upper=11)
        .rename("proj_yr")
    )

    model_points["tech_id"] = model_points["PRODUCT_ID"].map(
        product.set_index("PRODUCT_ID")["TECH_ASSUMPTION_ID"]
    )
    tech_ids_output = output["MP_ID"].map(
        model_points.set_index("MP_ID")["tech_id"]
    )
    t2 = pd.concat([tech_ids_output, projection_yr], axis=1)

    merged_df = pd.merge(
        t2,
        tech_assumptions,
        left_on=["MP_ID", "proj_yr"],
        right_on=["TECH_ASSUMPTION_ID", "PROJECTION_YR"],
        how="inner",
        validate="m:1",
    )

    return merged_df[col_name]


def npv(merged_df, values_to_project):
    """
    Calculate the Net Present Value (NPV) of projected values.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing merged data, including
            columns necessary for NPV calculation.
        values_to_project (str): Column name containing the values to project.

    Returns:
        pandas.Series: Series containing the calculated NPV for each row in the DataFrame.
    """
    annual_int_rate = merged_df["INT_RATE"]
    monthly_int_rate = (1 + annual_int_rate) ** (1 / 12) - 1
    discount_factor = 1 / (1 + monthly_int_rate) ** (
        merged_df["month_index"] + 1
    )

    npv = merged_df[values_to_project] * discount_factor
    npv_df = pd.DataFrame(
        {
            "NPV": npv,
            "MP_ID": merged_df["MP_ID"],
        }
    )

    npv_df = npv_df.iloc[::-1]
    grouped_data = npv_df.groupby("MP_ID")
    npv_df["van"] = grouped_data["NPV"].cumsum()
    npv_df = npv_df.iloc[::-1]

    return npv_df["van"] / discount_factor
