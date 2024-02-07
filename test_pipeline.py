import pytest
import pandas as pd
from pipeline import extract, transform

path = "https://raw.githubusercontent.com/jun-sylva/data/main/movies.csv"


def test_extract():
    df = extract(path)
    assert isinstance(df, pd.DataFrame)


# Check nan Values
def test_nan_values():
    df = extract(path)
    df = transform(df)
    assert df.isnull().sum().sum() == 0, "Dataset has nan value"


# Check blank Values
def test_blank_values():
    df = extract(path)
    df = transform(df)
    assert df.astype(str).applymap(str.strip).eq('').sum().sum() == 0, "Dataset has blank value"


# check if column genres is boolean
def test_boolean_values():
    df = extract(path)
    df = transform(df)
    column_bool = df['budget']
    assert all(isinstance(x, bool) for x in column_bool), "The column contains non-boolean values"
