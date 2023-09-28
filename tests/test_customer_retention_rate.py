import pandas as pd
from src.filter_by_year_and_quarter import filter_by_year_and_quarter
from src.customer_retention_rate import customer_retention_rate

def test_customer_retention_date(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    customer_retention_rate_result = customer_retention_rate(filtered_data)
    expected_result =  44.01
    assert customer_retention_rate_result == expected_result, f"The customer retention rate for {year} Q{quarter} should be f{expected_result}%"
