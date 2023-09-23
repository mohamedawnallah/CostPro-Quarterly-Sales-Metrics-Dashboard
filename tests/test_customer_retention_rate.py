import pandas as pd
from src.filter_by_year_and_quarter import *
from src.customer_retention_rate import *

def test_customer_retention_date(data: pd.DataFrame) -> float:
    year, quarter = 2022, 4
    filtered_data = filter_by_year_and_quarter(data, year, quarter)
    previous_quarter = quarter - 1 if quarter > 1 else 4
    previous_year = year if quarter > 1 else year - 1
    filtered_df_previous_quarter = data[(data['Year'] == previous_year) & (data['Quarter'] == previous_quarter)]
    customer_retention_rate_result = customer_retention_rate(filtered_data, filtered_df_previous_quarter)
    expected_result =  61.85
    assert customer_retention_rate_result == expected_result, f"The customer retention rate for {year} Q{quarter} should be f{expected_result}%"
