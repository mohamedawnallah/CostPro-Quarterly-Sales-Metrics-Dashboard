import pandas as pd
import pytest

@pytest.fixture
def data():
    return pd.read_csv("./data.csv")