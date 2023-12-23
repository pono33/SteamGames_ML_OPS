import pandas as pd

# Load DataFrames from Parquet files from the datasets folder
playtime_genre = pd.read_parquet('API/datasets_API/playtime_genre.parquet')
users_reviews = pd.read_parquet('API/datasets_API/users_reviews.parquet')

