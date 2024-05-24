from furtheredge.abstracted_packages import furtheredge_pandas as pd
from furtheredge.modules.universal_life.run import universal_life_module
import pkg_resources
from furtheredge.modules.universal_life.merge_all_df import (
    merge_all_dfs_police,
)
import time


def universal_life(
    chuck_size=100, projection_date="2023-10-31", projection_points=50
):
    """
    Perform calculations for a universal life insurance module.

    Returns:
    - DataFrame: DataFrame containing the output of the calculations.

    This function reads input data files, including model points, reinsurance rates,
    waiver of premium rates, technical assumptions, and product information. It then
    calls the universal_life_module function to perform calculations for the universal
    life insurance module using the input data and returns the output DataFrame.
    """
    package_dir = pkg_resources.resource_filename("furtheredge", "")

    model_points_path = package_dir + "/inputs/model_points2.csv"
    ri_rates_path = package_dir + "/inputs/ri_rates.csv"
    wop_rates_path = package_dir + "/inputs/wop_rates.csv"
    tech_assumptions_path = package_dir + "/inputs/tech_assumptions.csv"
    product_path = package_dir + "/inputs/product.csv"

    model_points = pd.read_csv(model_points_path)
    ri_rates = pd.read_csv(ri_rates_path, sep=";", decimal=",")
    wop_rates = pd.read_csv(wop_rates_path, sep=";", decimal=",")
    tech_assumptions = pd.read_csv(tech_assumptions_path, sep=";", decimal=",")
    product = pd.read_csv(product_path, sep=";", decimal=",")

    if chuck_size <= 0:
        output = merge_all_dfs_police(
            model_points,
            ri_rates,
            wop_rates,
            tech_assumptions,
            product,
            projection_date,
            projection_points,
        )
        result_universal_life, not_found_columns = universal_life_module(
            output
        )
        return result_universal_life, not_found_columns
    else:
        all_result_universal_life = pd.DataFrame()

        for chunk_start in range(0, len(model_points), chuck_size):
            chunk_end = min(chunk_start + chuck_size, len(model_points))
            chunk_model_points = model_points[chunk_start:chunk_end]
            output = merge_all_dfs_police(
                chunk_model_points,
                ri_rates,
                wop_rates,
                tech_assumptions,
                product,
                projection_date,
                projection_points,
            )
            result_universal_life, not_found_columns = universal_life_module(
                output
            )
            all_result_universal_life = pd.concat(
                [all_result_universal_life, result_universal_life],
                ignore_index=True,
            )
        return all_result_universal_life, not_found_columns
