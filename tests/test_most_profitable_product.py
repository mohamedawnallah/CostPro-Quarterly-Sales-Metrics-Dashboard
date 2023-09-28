import pandas as pd
from src.filter_by_year_and_quarter import filter_by_year_and_quarter
from src.most_profitable_product import most_profitable_product

def test_most_profitable_product(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    most_profitable_product_result = most_profitable_product(filtered_data)
    expected_result = "PAPER CRAFT , LITTLE BIRDIE"
    assert most_profitable_product_result == expected_result, f"The most profitable product for {year} Q{quarter} should be {expected_result}"
