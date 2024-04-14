from pipeline import extract, transform, export
import logging
from datetime import datetime

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

date_time = datetime.now().strftime("%Y-%m-%d_%H-%M")
file_name = f"Films_{date_time}.xlsx"
path_extract = "D:/data engineer/export/" + file_name
path = "https://raw.githubusercontent.com/jun-sylva/data/main/movies.csv"
try:
    df = extract(path)
    df_clean = transform(df)
    export(df_clean, path_extract)
    logging.info("Successfully extracted, transformed and loaded data.")
except Exception as e:
    logging.error(f"Pipeline failed with error: {e}")
