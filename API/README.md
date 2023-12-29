

# Directory Details
- **datasets_API/:** Contains Parquet files for game data.
- **init.py:** Initialization file for Python package.
- **data.py:** Module for loading datasets into Pandas DataFrames.
- **functions.py:** Module containing API functions for querying data.
- **main.py:** Main FastAPI application file.
- **recommendation_model.joblib:** Joblib file containing the recommendation model.
- **requirements.txt:** File listing project dependencies.
  
# Data Loading
The **data.py** module loads three DataFrames from Parquet files:

- **playtime_genre:** Contains information about playtime for each genre.
- **users_reviews:** Holds user reviews data.
- **df_games:** Stores general information about games.

# API Endpoints

1. _PlayTimeGenre_
/playtime_genre/{genre}

Finds the year with the most hours played for a specific genre.

2. _UserForGenre_
/user_for_genre/{genre}

Finds the user with the most hours played for a specific genre.

3. _UsersRecommend_
/users_recommend/{year}

Identifies the top 3 recommended games for a given year.

4. _UsersWorstDeveloper_
/users_worst_developer/{year}

Identifies the top 3 developers with the least recommended games for a given year.

5. _SentimentAnalysis_
/sentiment_analysis/{developer_company}

Counts the number of negative, neutral, and positive reviews for a specified developer.

6. _GameRecommendations_
/game_recommendations/{item_id}

Provides recommendations for games similar to a given game based on a K-nearest neighbors approach.

# Getting Started
Install dependencies: pip install -r requirements.txt
Run the FastAPI application: uvicorn main:app --reload
