import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.pipeline import Pipeline

# Datasets import
from data import playtime_genre, users_reviews, df_games

# Model import
pipeline = joblib.load('recommendation_model.joblib')

# API Functions:    

def PlayTimeGenre( genre : str ):
    """
    Finds the year with the most hours played for a specific genre, ignoring case and checking data types.

    Args:
        genre: The genre to search for (str).

    Returns:
        A dictionary with information about the genre and the year in wich was most played.
    """
    
    # Ensure proper data types
    if not isinstance(genre, str):
        raise TypeError(f"Expected 'genre' to be a string, got {type(genre)}.")

    # Case-insensitive genre search
    filtered_playtime = playtime_genre[playtime_genre["genre"].str.lower() == genre.lower()]

    # Check for empty results
    if not filtered_playtime.empty:
        # Find year with most playtime
        max_playtime_year = filtered_playtime.groupby("year")["playtime"].sum().idxmax()

        # Build and return dictionary
        return {
            f"Release year with the most hours played for Genre '{genre.capitalize()}'": int(max_playtime_year)
        }
    else:
        return f"No Year was found in which the Genre '{genre.capitalize()}' was played"
    

def UserForGenre( genre : str ):
    """
    Finds the user with the most hours played for a specific genre, ignoring case and checking data types.

    Args:
        genre: The genre to search for (str).

    Returns:
        A dictionary with information about the user and their playtime.
    """

    # Ensure proper data types
    if not isinstance(genre, str):
        raise TypeError(f"Expected 'genre' to be a string, got {type(genre)}.")

    # Case-insensitive genre search
    filtered_playtime = playtime_genre[playtime_genre["genre"].str.lower() == genre.lower()]

    # Check for empty results
    if not filtered_playtime.empty:
        # Find user with most playtime
        max_playtime_user = filtered_playtime.groupby("user_id")["playtime"].sum().idxmax()

        # Get year-wise playtime accumulation
        yearly_hour_accumulation = (
            filtered_playtime[filtered_playtime["user_id"] == max_playtime_user]
            .groupby("year")["playtime"]
            .sum()
            .reset_index()
            .to_dict(orient="records")
        )

        # Build and return dictionary
        return {
            f"User with highiest playtime hours '{genre.capitalize()}'": max_playtime_user,
            "Playtime Hours": yearly_hour_accumulation,
        }
    else:
        return f"No Year was found in which the Genre '{genre.capitalize()}' was played"
    
    
def UsersRecommend( year : int ):
    """
    Identifies the top 3 recommended games for a given year.

    Args:
        year: The year to search for (int).

    Returns:
        A dictionary with information about the 3 top games.
    """

    # Ensure proper data types
    if not isinstance(year, int):
        raise TypeError(f"Expected 'year' to be an integer, got {type(year)}.")

    # Filter the users_reviews DataFrame for the given year, where the recommendations are True and the sentiment_analysis is 1 or 2
    filtered_reviews = users_reviews.query("year == @year and recommend and sentiment_analysis in [1, 2]")
    
    # Check for empty results
    if not filtered_reviews.empty:
        # Get top 3 games most recomended
        top_games = filtered_reviews['title'].value_counts().head(3).index

    # Build and return dictionary
        return [{"{}° place".format(i+1): game} for i, game in enumerate(top_games)]
        
    else:
        return f"No games found for the year entered: '{year}'"
    

def UsersWorstDeveloper( year : int ):
    """
    Identifies the top 3 developer with the less recommended games for a given year.

    Args:
        year: The year to search for (int).

    Returns:
        A dictionary with information about the 3 worst developers.
    """

    # Ensure proper data types
    if not isinstance(year, int):
        raise TypeError(f"Expected 'year' to be an integer, got {type(year)}.")

    # Filter the users_reviews DataFrame for the given year, where the recommendations are False and the sentiment_analysis is 0
    filtered_developers = users_reviews.query("year == @year and recommend == False and sentiment_analysis == 0")
    
    # Check for empty results
    if not filtered_developers.empty:
        # Get the 3 worst developers
        worst_developers = filtered_developers['developer'].value_counts().head(3).index

    # Build and return dictionary
        return [{"{}° place".format(i+1): developer} for i, developer in enumerate(worst_developers)]
        
    else:
        return f"No developers found for the year entered: '{year}'"
    

def sentiment_analysis( developer_company : str ):
    """
    Count the number of negative, neutral, and positive reviews clasified by a previous sentiment analysis for the specified developer.

    Args:
        empresa_desarrolladora: The developer to search for (str).

    Returns:
        A nested dictionary with the developer's name as the key and a list with the total number of user's review records that are categorized with a sentiment analysis value.
    """

    # Ensure proper data types
    if not isinstance(developer_company, str):
        raise TypeError(f"Expected 'developer_company' to be a string, got {type(developer_company)}.")

    # Case-insensitive developer search
    developer = developer_company.lower()
    reviews_for_developer = users_reviews[users_reviews["developer"].str.lower() == developer]

    # Check for empty results
    if not reviews_for_developer.empty:
        # Count the number of review records with sentiment analysis
        sentiment_counts = reviews_for_developer['sentiment_analysis'].value_counts().to_dict()

        # Crear el diccionario con el formato deseado
        return {developer_company: {
            'Negative': sentiment_counts.get(0, 0),
            'Neutral': sentiment_counts.get(1, 0),
            'Positive': sentiment_counts.get(2, 0)
        }}

    else:
        return f"No developers found for the year entered: '{developer_company}'"
    

def game_recommendations( item_id : int ):
    '''
    This function helps users discover games that are similar to a given game (specified by item_id)
    by employing a K-nearest neighbors approach after transforming the input data.

    Args:
        item_id: from the game of wich we want to get recommendations based on (6 digits int).

    Returns: 
        The generated dictionary of recommendations.
    '''
    # Ensure proper data types
    if not isinstance(item_id, int) or not (000000 <= item_id <= 999999):
        raise TypeError(f"Expected 'item_id' to be an 6-digit integer, got {type(item_id)}.")

    # Check if item_id is in the data to be analyzed
    if item_id not in df_games['item_id'].values:
        return {'error': 'item_id not found in the database.'}

    # Find the index of the game in the DataFrame based on the item_id
    game_info = df_games[df_games['item_id'] == item_id]

    # Transform the game information with the preprocessor
    transformed_input = pipeline.named_steps['preprocessor'].transform(game_info)

    # Find the nearest games using KNN
    distances, indices = pipeline.named_steps['knn_model'].kneighbors(transformed_input)

    # Filter the current game
    distances = distances.flatten()[1:]
    indices = indices.flatten()[1:]

    # Get recommended titles
    recommended_titles = df_games.loc[indices, 'title'].tolist()

    # Build and return dictionary
    return [{'{}'.format(i + 1): title} for i, title in enumerate(recommended_titles)]
