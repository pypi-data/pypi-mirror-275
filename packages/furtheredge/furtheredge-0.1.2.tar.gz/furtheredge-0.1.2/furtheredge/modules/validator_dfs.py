def check_columns_existence(df, list_of_columns_name):
    """
    Check if all columns exist inside the DataFrame.

    Args:
    - df (DataFrame): The DataFrame to check columns against.
    - list_of_columns_name (list): List of column names to check.

    Returns:
    - tuple: A tuple containing a boolean indicating whether all columns exist and a list of columns not found.

    This function checks if all columns specified in the list_of_columns_name exist inside the DataFrame (df).
    It returns a tuple with a boolean value indicating whether all columns exist and a list of columns not found.
    If all columns are found, the boolean value is True and the list of columns not found is empty ([]).
    If some columns are missing, the boolean value is False and the list contains the names of the columns not found.
    """
    columns_not_found = [
        col for col in list_of_columns_name if col not in df.columns
    ]

    if not columns_not_found:
        return True, []
    else:
        return False, columns_not_found
