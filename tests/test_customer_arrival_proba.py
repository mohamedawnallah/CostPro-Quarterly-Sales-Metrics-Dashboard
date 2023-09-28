import pandas as pd
from src.customer_arrival_proba import customer_arrival_proba
from src.filter_by_year_and_quarter import filter_by_year_and_quarter

def test_customer_arrival_proba(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    dist = customer_arrival_proba(filtered_data)
    k = len(filtered_data['CustomerID'].unique()) * 1.1
    probability = dist.pmf(k)
    assert probability == 0.0, 'There should be no customers for 2022 Q4'
