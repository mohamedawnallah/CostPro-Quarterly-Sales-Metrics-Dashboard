import pandas as pd
from src.filter_by_year_and_quarter import filter_by_year_and_quarter
from src.order_value_variability import order_value_variability

def test_order_value_variability(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    order_value_variability_result = order_value_variability(filtered_data)
    expected_result = 2461.58
    assert order_value_variability_result == expected_result, f"The order value variability for {year} Q{quarter} should be {expected_result}$"
