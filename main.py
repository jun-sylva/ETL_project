from pipeline import extract
import logging

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

path = "https://raw.githubusercontent.com/jun-sylva/data/main/movies.csv"
try:
    df = extract(path)
    print(df.dtypes)
    logging.info("Successfully extracted, transformed and loaded data.") # Log success message
except Exception as e:
    logging.error(f"Pipeline failed with error: {e}")
