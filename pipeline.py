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

    """
    Modeling column 'production_companies' ({'name': 'Pixar Animation Studios', 'id': 3}, {'name': 'Warner Bros.', 'id': 6194})
    to ['Pixar Animation Studios', 'Warner Bros.']
    """
    df['production_companies'] = df['production_companies'].apply(lambda x: re.findall(r"'name': '([^']+)'", x))
    df['production_companies'] = df['production_companies'].astype(str)
    df = df.copy()

    """
    Modeling column 'production_countries' ({'iso_3166_1': 'US', 'name': 'United States of America'}, {'iso_3166_1': 'DE', 'name': 'Germany'})
    to ['Pixar Animation Studios', 'Warner Bros.']
    """
    df['production_countries'] = df['production_countries'].apply(lambda x: re.findall(r"'name': '([^']+)'", x))
    df['production_countries'] = df['production_countries'].astype(str)
    df = df.copy()

    """
    Modeling column 'production_countries' ({'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'})
    to ['English', 'Français']
    """
    df['spoken_languages'] = df['spoken_languages'].apply(lambda x: re.findall(r"'name': '([^']+)'", x))
    df['spoken_languages'] = df['spoken_languages'].astype(str)
    df = df.copy()

    # Modeling column 'popularity' (convert to float and delete incorrect value)
    df["popularity"] = pd.to_numeric(df["popularity"], errors='coerce')
    df = df[df["popularity"].notnull() & df["popularity"].astype(float).apply(lambda x: isinstance(x, float))]
    df["popularity"] = df["popularity"].round(2)
    df = df.copy()

    # Modeling column 'release_date' (convert to datetime and delete incorrect value)
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df = df[df['release_date'].notnull()]
    df['release_date'] = df['release_date'].dt.year
    df = df.copy()

    # Convert columns types to float if the type is different
    df[['revenue', 'vote_average', 'vote_count']] = df[['revenue', 'vote_average', 'vote_count']].astype(float)

    return df
