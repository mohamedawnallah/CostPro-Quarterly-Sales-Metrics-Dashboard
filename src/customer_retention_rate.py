import pandas as pd

# @title
def customer_retention_rate(data: pd.DataFrame, previous_quarter_data: pd.DataFrame) -> float:
    """
    Calculate the customer retention rate for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the customer retention rate for
    :param quarter: The quarter to calculate the customer retention rate for
    :return: The customer retention rate for the given year and quarter
    """    
    specified_quarter_customers = set(data['CustomerID'].unique())
    
    previous_quarter_customers = set(previous_quarter_data['CustomerID'].unique())

    retained_customers = len(specified_quarter_customers.intersection(previous_quarter_customers))
    previous_quarter_customer_count = len(previous_quarter_customers)

    if previous_quarter_customer_count > 0:
        retention_rate = (retained_customers / previous_quarter_customer_count) * 100
        return round(retention_rate, 2)
    else:
        return None