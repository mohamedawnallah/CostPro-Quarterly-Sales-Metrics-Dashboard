import pandas as pd
from src.filter_by_year_and_quarter import filter_by_year_and_quarter
from src.most_popular_product import most_popular_product

def test_most_popular_product(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    most_popular_product_result = most_popular_product(filtered_data)
    expected_result = "PAPER CRAFT , LITTLE BIRDIE"
    assert most_popular_product_result == expected_result, f"The most popular product for {year} Q{quarter} should be {expected_result}"
