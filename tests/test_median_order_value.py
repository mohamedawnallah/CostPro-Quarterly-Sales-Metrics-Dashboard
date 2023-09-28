import pandas as pd
from src.filter_by_year_and_quarter import filter_by_year_and_quarter
from src.median_order_value import median_order_value

def test_median_order_value(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    median_order_value_result = median_order_value(filtered_data)
    expected_result = 304.72
    assert median_order_value_result == expected_result, f"The median order value for {year} Q{quarter} should be {expected_result}$"
