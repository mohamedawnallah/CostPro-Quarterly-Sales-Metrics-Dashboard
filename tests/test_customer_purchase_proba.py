import pandas as pd
from src.customer_purchase_proba import customer_purchase_proba
from src.filter_by_year_and_quarter import filter_by_year_and_quarter

def test_customer_purchase_proba(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    dist = customer_purchase_proba(filtered_data)
    customer_purchase_high_value_sale_probability = round(1 - dist.cdf(349),2)
    assert customer_purchase_high_value_sale_probability == 0.99, 'There should be 99% probability for getting at least 350 high sale in 2022 Q4'
