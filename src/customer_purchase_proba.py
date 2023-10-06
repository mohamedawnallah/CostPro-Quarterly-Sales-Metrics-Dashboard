import pandas as pd
from scipy.stats import binom
import numpy as np
# Write a function using the Binomial distribution to model the number of sales
def customer_purchase_proba(data: pd.DataFrame) -> float:
    """
    Calculate the probability of a customer arriving on the website in the next 15 minutes
    :param data: The dataframe containing the data
    :param year: The year to calculate the probability for
    :param quarter: The quarter to calculate the probability for
    :return: The probability of a customer arriving on the website in the next 15 minutes
    """
    sales_unique = data['InvoiceNo'].nunique()
    high_value_sales_count = (data.groupby('InvoiceNo')['TotalPrice'].sum() > 1000).sum()
    high_value_sale_probability = high_value_sales_count / sales_unique
    dist = binom(n=sales_unique, p=high_value_sale_probability)
    return dist
