import pandas as pd

# @title
# Write a function to find the most profitable product for a given year and quarter
def most_profitable_product(data: pd.DataFrame) -> str:
    """
    Find the most profitable product for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to find the most profitable product for
    :param quarter: The quarter to find the most profitable product for
    :return: The most profitable product for the given year and quarter
    """
    # Find the most profitable product
    return data.groupby("Description")["TotalPrice"].sum().idxmax()