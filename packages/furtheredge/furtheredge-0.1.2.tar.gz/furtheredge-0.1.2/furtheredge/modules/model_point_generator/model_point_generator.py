from furtheredge.abstracted_packages import furtheredge_numpy as np
from furtheredge.abstracted_packages import furtheredge_pandas as pd

from furtheredge.modules.model_point_generator.policies_refinement import (
    load_rename_policies_columns,
)


def generate_model_points(
    path_policies_file,
    json_path,
    pivot_config,
):
    # Initialize index, values lists and modelpoints DataFrame
    index_list = []
    values_dict = {}
    modelpoints = pd.DataFrame()

    policies = load_rename_policies_columns(path_policies_file, json_path)

    # Iterate over dictionary items
    for col, agg_func in pivot_config.items():
        if col not in policies.columns:
            print(
                f"Warning: '{col}' is not present in the Policies DataFrame."
            )
            continue

        if agg_func.startswith("USED_DIRECT"):
            index_list.append(col)
        elif agg_func.startswith("USED_AGG"):
            agg_type = agg_func.split("_")[2]
            values_dict[col] = agg_type.lower()

    # Construct pivot table if there are columns to pivot on
    if len(index_list) > 0:
        modelpoints = policies.pivot_table(
            index=index_list,
            values=list(values_dict.keys()),
            aggfunc=values_dict,
        ).reset_index()
    else:
        print("No valid columns found to create a pivot table.")

    modelpoints.insert(0, "MP_ID", np.arange(1, len(modelpoints) + 1))
    product_id_map = {
        "EDB": 1,
        "EDM": 2,
        "EDU": 3,
        "OLB": 4,
        "OLF": 5,
        "OLG": 6,
        "OLM": 7,
    }
    modelpoints.insert(
        2, "PRODUCT_ID", modelpoints["PLAN_CODE"].map(product_id_map)
    )

    return modelpoints
