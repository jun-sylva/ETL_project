import pytest
import pandas as pd
from pipeline import extract

path = "https://raw.githubusercontent.com/jun-sylva/data/main/movies.csv"
def test_extract():
    df = extract(path)
    assert isinstance(df, pd.DataFrame)