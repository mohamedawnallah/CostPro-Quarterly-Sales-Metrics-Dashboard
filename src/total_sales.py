import pandas as pd

# @title
def total_sales(data: pd.DataFrame) -> float:
    """
    Calculate the total sales for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the total sales for
    :param quarter: The quarter to calculate the total sales for
    :return: The total sales for the given year and quarter
    """
    # Calculate the total sales
    return data['TotalPrice'].sum().round(2)