import pandas as pd

# Load DataFrames from Parquet files from the datasets folder
playtime_genre = pd.read_parquet('datasets_API/playtime_genre.parquet')
users_reviews = pd.read_parquet('datasets_API/users_reviews.parquet')
df_games = pd.read_parquet('datasets_API/df_games_model.parquet')