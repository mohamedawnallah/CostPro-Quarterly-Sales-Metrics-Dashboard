import pandas as pd
from src.customer_arrival_proba import customer_arrival_proba
from src.filter_by_year_and_quarter import filter_by_year_and_quarter

def test_customer_arrival_proba(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    dist = customer_arrival_proba(filtered_data)
    avg_customers = filtered_data.groupby(['Year', 'Month', 'Day'])['CustomerID'].nunique().mean()
    k = int(avg_customers * 1.1)
    probability = round(dist.pmf(k),2)
    assert probability == 0.03, 'There should be 3% for 10% more than average customers per day for 2022 Q4'
