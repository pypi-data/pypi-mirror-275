from furtheredge.abstracted_packages import furtheredge_pandas as pd
from furtheredge.abstracted_packages import furtheredge_json as json


def load_json_to_dict(file_path):
    with open(file_path, "r") as file:
        mapping_dict = json.load(file)
    return mapping_dict


def rename_columns(dataframe, mapping_dict):
    renamed_columns = {v: k for k, v in mapping_dict.items()}
    dataframe_renamed = dataframe.rename(columns=renamed_columns)

    return dataframe_renamed


def load_rename_policies_columns(policies_file_path, json_path):

    mapping_dict = load_json_to_dict(json_path)
    df_policies = pd.read_csv(policies_file_path)
    policies_renamed_df = rename_columns(df_policies, mapping_dict)
    return policies_renamed_df
