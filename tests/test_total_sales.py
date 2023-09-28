import pandas as pd
from src.filter_by_year_and_quarter import filter_by_year_and_quarter
from src.total_sales import total_sales

def test_total_sales(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    total_sales_result = total_sales(filtered_data)
    expected_result = 2719328.96
    assert total_sales_result == expected_result, f"The total sales for {year} Q{quarter} should be {expected_result}$"
