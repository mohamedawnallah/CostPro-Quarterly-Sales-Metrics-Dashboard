import pandas as pd

# @title
# Write a function to calculate mean number of customers per day
def mean_customers_per_day(data: pd.DataFrame) -> float:
    """
    Calculate the mean number of customers per day for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the mean number of customers per day for
    :param quarter: The quarter to calculate the mean number of customers per day for
    :return: The mean number of customers per day for the given year and quarter
    """
    # Calculate the mean number of customers per day
    return data.groupby(['Month', 'Day'])['CustomerID'].nunique().mean().round(2)