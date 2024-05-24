from furtheredge.abstracted_packages import furtheredge_pandas as pd

from furtheredge.modules.universal_life.sub_modules.duration import (
    duration_calculation,
)
from furtheredge.modules.universal_life.sub_modules.reserve import (
    reserve_calculation,
)
from furtheredge.modules.universal_life.sub_modules.proba import (
    proba_calculation,
)
from furtheredge.modules.universal_life.sub_modules.prospective import (
    prospective_calculation,
)
from furtheredge.modules.universal_life.required_data_calculation import (
    required_columns_duration,
    required_columns_proba,
    required_columns_prospective,
    required_columns_reserve,
)
from furtheredge.modules.validator_dfs import check_columns_existence
from furtheredge.modules.universal_life.merge_all_df import (
    merge_all_dfs_police,
)


dict_functions_mapping = {
    "duration": duration_calculation,
    "reserve": reserve_calculation,
    "proba": proba_calculation,
    "prospective": prospective_calculation,
}


def sub_module_process(
    merged_df,
    required_columns,
    not_found_columns,
    sub_module_name,
    # model_points,
    # tech_assumptions,
    # ri_rates,
    # wop_rates,
    # product,
    # projection_date,
    # projection_points,
):
    validator, not_found_columns_process = check_columns_existence(
        merged_df, required_columns
    )

    if sub_module_name in dict_functions_mapping:
        if validator:
            merged_df = dict_functions_mapping[sub_module_name](merged_df)
            not_found_columns.append(
                {
                    "process_name": sub_module_name,
                    "columns_not_found": not_found_columns_process,
                }
            )
        else:
            not_found_columns.append(
                {
                    "process_name": sub_module_name,
                    "columns_not_found": not_found_columns_process,
                }
            )
    return not_found_columns, merged_df


# run_settings: { projection_date: DATE-STRING, time_horizon: int, simulation_number: int, scenario_id: string }
def universal_life_module(output):
    """
    Perform calculations for a universal life insurance module.

    Args:
    - model_points (DataFrame): DataFrame containing model points data.
    - run_settings (dict): Dictionary containing settings for the run.
    - tech_assumptions (DataFrame): DataFrame containing technical assumptions.
    - ri_rates (DataFrame): DataFrame containing reinsurance rates.
    - wop_rates (DataFrame): DataFrame containing waiver of premium rates.
    - product (str): Name of the product.

    Returns:
    - DataFrame: DataFrame containing the output of the calculations.

    This function performs various calculations for a universal life insurance module,
    including duration calculation, reserve calculation, probability calculation,
    and prospective calculation. It initializes an output DataFrame with model points
    and projection duration, performs the calculations, and returns the output DataFrame.
    """

    not_found_columns = []

    not_found_columns, output = sub_module_process(
        output,
        required_columns_duration,
        not_found_columns,
        "duration",
    )
    not_found_columns, output = sub_module_process(
        output,
        required_columns_reserve,
        not_found_columns,
        "reserve",
    )
    not_found_columns, output = sub_module_process(
        output,
        required_columns_proba,
        not_found_columns,
        "proba",
    )
    not_found_columns, output = sub_module_process(
        output,
        required_columns_prospective,
        not_found_columns,
        "prospective",
    )

    return output, not_found_columns
