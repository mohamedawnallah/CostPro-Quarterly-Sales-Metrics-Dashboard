import pandas as pd

# @title
def customer_retention_rate(data: pd.DataFrame) -> float:
    """
    Calculate the customer retention rate for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the customer retention rate for
    :param quarter: The quarter to calculate the customer retention rate for
    :return: The customer retention rate for the given year and quarter
    """    
    invoices_count = data.groupby('CustomerID')['InvoiceNo'].nunique()
    num_customers = len(invoices_count)
    num_repeat_customers = len(invoices_count[invoices_count >1])
    return round((num_repeat_customers / num_customers) * 100, 2)
