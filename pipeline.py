import pandas as pd
import re


def extract(path):
    df = pd.read_csv(path, low_memory=False)
    return df


def transform(df):
    # Delete unused columns
    df = df[['adult', 'budget', 'genres', 'popularity', 'production_companies', 'production_countries',
             'release_date', 'revenue', 'spoken_languages', 'title', 'vote_average', 'vote_count']]
    df = df.copy()

    # Delete rows with NaN value
    df = df.dropna(axis=0)
    df = df.copy()

    # Delete rows when column 'adult' is not True or False
    df = df.loc[df['adult'].isin([True, False])]
    df['adult'] = df['adult'].astype(bool)
    df = df.copy()

    # Convert type of column budget
    df["budget"] = df["budget"].astype('Int64')

    """
    Modeling column 'genres' ({'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'})
    to ['Animation', 'Comedy']
    """
    df['genres'] = df['genres'].apply(lambda x: re.findall(r"'name': '([^']+)'", x))
    df['genres'] = df['genres'].astype(str)
    df = df.copy()

    # Modeling column 'popularity' (convert to fload and delete incorrect value)
    df["popularity"] = pd.to_numeric(df["popularity"], errors='coerce')
    df = df[df["popularity"].notnull() & df["popularity"].astype(float).apply(lambda x: isinstance(x, float))]
    df["popularity"] = df["popularity"].round(2)
    df = df.copy()

    return df
