import pandas as pd

# @title
# Write a function to find the most popular product for a given year and quarter
def most_popular_product(data: pd.DataFrame) -> str:
    """
    Find the most popular product for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to find the most popular product for
    :param quarter: The quarter to find the most popular product for
    :return: The most popular product for the given year and quarter
    """
    # Find the most popular product
    return data.groupby('Description')['Quantity'].sum().idxmax()

