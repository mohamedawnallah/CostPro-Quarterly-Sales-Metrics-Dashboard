import pandas as pd
from src.customer_purchase_proba import customer_purchase_proba
from src.filter_by_year_and_quarter import filter_by_year_and_quarter

def test_customer_purchase_proba(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    dist = customer_purchase_proba(filtered_data)
    customer_purchase_high_value_sale_probability = 1 - dist.cdf(349)
    assert customer_purchase_high_value_sale_probability == 0.0, 'There is no high value sale customer purchase in 2022 Q4'
