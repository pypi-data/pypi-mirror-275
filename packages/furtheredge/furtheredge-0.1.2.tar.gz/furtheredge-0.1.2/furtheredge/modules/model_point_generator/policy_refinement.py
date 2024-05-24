import numpy as np
import pandas as pd
import json


def policy_refinement(polices, run_settings):

    # Projection Date
    with open(r"data\projectiondate.txt", "r") as file:
        # Read the content of the file
        projection_date = file.read()

    polices = pd.read_csv(r"data\policies.csv", low_memory=False)

    polices["DOB"] = pd.to_datetime(polices["DOB"])
    polices["Inception Date"] = pd.to_datetime(polices["Inception Date"])
    polices["Maturity Date"] = pd.to_datetime(polices["Maturity Date"])

    new_policy = pd.DataFrame()

    fixed_projection_date = pd.to_datetime(projection_date)

    # Calculate difference in months
    new_policy["DURATIONIF_M"] = (
        (fixed_projection_date - polices["Inception Date"])
        / pd.Timedelta(days=1)
        / 30
    ).astype(int)
    new_policy["POLICY_TERM_M"] = (
        (polices["Maturity Date"] - polices["Inception Date"])
        / pd.Timedelta(days=1)
        / 30
    ).astype(int)

    new_policy["PRODUCT_NAME"] = "Universal Life"

    pol = pd.read_excel(
        io=r"data\policyinputstructure.xlsx", sheet_name="POLICY"
    )

    for index, row in pol.iterrows():
        if row["From Data Received to POLICY Tab"] == "DIRECT":
            new_name = row["Variable"]
            old_name = row["Label in Excel file"]
            new_policy[new_name] = polices[old_name]

    column_order = pol["Variable"].to_list()
    new_policy = new_policy[column_order]

    # Convert dtypes to dictionary
    dtypes_dict = pol.dtypes.apply(lambda x: x.name).to_dict()

    # Save dtypes as a dictionary to a JSON file
    with open(r"data\policy_dtypes.json", "w") as f:
        json.dump(dtypes_dict, f)

    new_policy.to_csv(r"data\new_policies.csv", index=False)

    return new_policy


def get_data_mapping(dataframe1, column1, column2):
    mapping_dict = dict(zip(dataframe1[column1], dataframe1[column2]))
    mapping_dict = {k: v for k, v in mapping_dict.items() if pd.notnull(v)}
    return mapping_dict


def rename_columns(dataframe2, mapping_dict):
    renamed_columns = {v: k for k, v in mapping_dict.items()}
    dataframe2_renamed = dataframe2.rename(columns=renamed_columns)

    return dataframe2_renamed


def load_policy_struct(file_path, sheet_name):
    mp = pd.read_excel(io=file_path, sheet_name=sheet_name)
    return mp


df_columns_mapping = load_policy_struct("policyinputstructure2.xlsx", "POLICY")

json_data = get_data_mapping(
    df_columns_mapping, "Variable", "Label in Excel file"
)

with open("sample.json", "w") as outfile:
    json.dump(json_data, outfile)

with open("sample.json", "r") as file:
    mapping_dict = json.load(file)

mapping_dict

df_policies_excel = pd.read_excel("policies.xlsx")

df_policies_excel.to_csv("policies.csv", index=False)

df_policies = pd.read_csv("policies.csv")

df_policies

output_df = rename_columns(df_policies, mapping_dict)

output_df

output_df.columns
