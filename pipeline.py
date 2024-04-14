import pandas as pd
import re
from datetime import datetime


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

    # Convert column 'adult' to bool
    #df['adult'] = df['adult'].astype(bool)
    #df = df.copy()

    # Convert type of column budget
    df["budget"] = df["budget"].astype('Int64')

    """
    Modeling column 'genres' ({'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'})
    to ['Animation', 'Comedy']
    """
    df['genres'] = df['genres'].astype(str)
    df['genres'] = df['genres'].apply(lambda x: re.findall(r"'name': '([^']+)'", x))
    df = df.copy()

    """
    Modeling column 'production_companies' ({'name': 'Pixar Animation Studios', 'id': 3}, 
    {'name': 'Warner Bros.', 'id': 6194})
    to ['Pixar Animation Studios', 'Warner Bros.']
    """
    df['production_companies'] = df['production_companies'].astype(str)
    df['production_companies'] = df['production_companies'].apply(lambda x: re.findall(r"'name': '([^']+)'", x))
    df = df.copy()

    """
    Modeling column 'production_countries' ({'iso_3166_1': 'US', 'name': 'United States of America'}, 
    {'iso_3166_1': 'DE', 'name': 'Germany'})
    to ['Pixar Animation Studios', 'Warner Bros.']
    """
    df['production_countries'] = df['production_countries'].astype(str)
    df['production_countries'] = df['production_countries'].apply(lambda x: re.findall(r"'name': '([^']+)'", x))
    df = df.copy()

    """
    Modeling column 'production_countries' ({'iso_639_1': 'en', 'name': 'English'}, 
    {'iso_639_1': 'fr', 'name': 'Français'})
    to ['English', 'Français']
    """
    df['spoken_languages'] = df['spoken_languages'].astype(str)
    df['spoken_languages'] = df['spoken_languages'].apply(lambda x: re.findall(r"'name': '([^']+)'", x))
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


def export(df, path_extract):
    adult = df.loc[df['adult'] == 'True']
    no_adult = df.loc[df['adult'] == 'False']
    film_comedy = df[df['genres'].apply(lambda x: 'Comedy' in x)]
    film_action = df[df['genres'].apply(lambda x: 'Action' in x)]
    film_horror = df[df['genres'].apply(lambda x: 'Horror' in x)]
    # Release date < 2000 and sort by DSC
    old_film = df.loc[df['release_date'] < 2000]
    old_film = old_film.sort_values(by='release_date', ascending=False)
    # Release date >= 2000 and sort by DSC
    film_2000 = df.loc[df['release_date'] >= 2000]
    film_2000 = film_2000.sort_values(by='release_date', ascending=False)
    # best_popularity >= 75.0 and sort by DSC
    best_popularity = df.loc[df['popularity'] >= 75.0]
    best_popularity = best_popularity.sort_values(by='popularity', ascending=False)
    # best average >= 5.0 and sort by DSC
    best_avg = df.loc[df['vote_average'] >= 5.0]
    best_avg = best_avg.sort_values(by='vote_average', ascending=False)
    # Create file excel
    with pd.ExcelWriter(path_extract) as films:
        adult.to_excel(films, sheet_name="Adult", index=False)
        no_adult.to_excel(films, sheet_name="No_adult", index=False)
        film_comedy.to_excel(films, sheet_name="Comedy", index=False)
        film_action.to_excel(films, sheet_name="Action", index=False)
        film_horror.to_excel(films, sheet_name="Horror", index=False)
        old_film.to_excel(films, sheet_name="Old_film(<2000)", index=False)
        film_2000.to_excel(films, sheet_name="Old_film(>=2000)", index=False)
        best_popularity.to_excel(films, sheet_name="Best_popularity(>=75.0)", index=False)
        best_avg.to_excel(films, sheet_name="Best_AVG(>=5.0)", index=False)
    return
