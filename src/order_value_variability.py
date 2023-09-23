import pandas as pd

# @title
# Write a function to calculate the order value variability for a given year and quarter
def order_value_variability(data: pd.DataFrame) -> float:
    """
    Calculate the order value variability for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the order value variability for
    :param quarter: The quarter to calculate the order value variability for
    :return: The order value variability for the given year and quarter
    """
    # Group data by order number and calculate the order total
    return data.groupby("InvoiceNo")['TotalPrice'].sum().std().round(2)