import pandas as pd
from src.filter_by_year_and_quarter import filter_by_year_and_quarter

def test_filter_by_year_and_quarter(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    years_unique_filtered_result = filter_by_year_and_quarter(data, year, quarter)['Year'].unique()[0]
    quarters_unique_filtered_result = filter_by_year_and_quarter(data, year, quarter)['Quarter'].unique()[0]
    assert years_unique_filtered_result == year, f"There should only be records for {year}"
    assert quarters_unique_filtered_result == quarter, f"There should be records for Q{quarter}"
