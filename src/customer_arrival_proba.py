import pandas as pd
from scipy.stats import poisson

# Write a function using the Poisson distribution to model how likely a customer is to arrive on the website in the next 15 minutes
def customer_arrival_proba(data: pd.DataFrame) -> float:
    """
    Calculate the probability of a customer arriving on the website in the next 15 minutes
    :param data: The dataframe containing the data
    :param year: The year to calculate the probability for
    :param quarter: The quarter to calculate the probability for
    :return: The probability of a customer arriving on the website in the next 15 minutes
    """
    mu = data.groupby(['Year', 'Month', 'Day']).agg(TotalCustomers=('CustomerID', 'nunique')).mean()[0]
    dist = poisson(mu=mu)
    return dist