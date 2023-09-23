import pandas as pd
from src.filter_by_year_and_quarter import *
from src.mean_customers_per_day import *

def test_mean_customers_per_day(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    mean_customers_per_day_result = mean_customers_per_day(filtered_data)
    expected_result = 74.8
    assert mean_customers_per_day_result == expected_result, f"The mean customers per day for {year} Q{quarter} should be {expected_result}$"
