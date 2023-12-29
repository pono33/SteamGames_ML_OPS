import pandas as pd

# Load DataFrames from Parquet files
playtime_genre = pd.read_parquet('datasets_API/playtime_genre.parquet', engine='pyarrow')
users_reviews = pd.read_parquet('datasets_API/users_reviews.parquet', engine='pyarrow')
df_games = pd.read_parquet('datasets_API/df_games_model.parquet', engine='pyarrow')