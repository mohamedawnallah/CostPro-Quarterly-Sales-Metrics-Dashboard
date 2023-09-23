import pandas as pd

# @title
# Write a function to calculate the median order value for a given year and quarter
def median_order_value(data: pd.DataFrame) -> float:
    """
    Calculate the median order value for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the median order value for
    :param quarter: The quarter to calculate the median order value for
    :return: The median order value for the given year and quarter
    """
    # Group data by order number and calculate the order total
    return data.groupby('InvoiceNo')['TotalPrice'].sum().median()