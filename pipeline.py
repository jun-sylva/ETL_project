import pandas as pd


def extract(path):
    df = pd.read_csv(path, low_memory=False)
    return df
