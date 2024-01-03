# <h1 align=center> **Steam Games Querys API** </h1>

Welcome to the Steam Games Querys API project! This API is designed to provide specific queries from a Steam dataset, which can be updated as needed. It is optimized for deployment on the free Render service, which offers 512MB of memory usage. Depending on the size of the datasets, you may need to upgrade to a paid Render plan with more memory processing capacity. This API was developed using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

Access my [Steam Games Querys API](https://steam-games-querys.onrender.com)

# Directory Details
- **datasets_API/** Contains Parquet files for game data.
- **init.py:** Initialization file for Python package.
- **data.py:** Module for loading datasets into Pandas DataFrames.
- **functions.py:** Module containing API functions for querying data.
- **main.py:** Main FastAPI application file.
- **recommendation_model.joblib:** Joblib file containing the recommendation model.
- **requirements.txt:** File listing project dependencies.

# Overview of Project Components

## data.py

**Purpose:** 
This module serves as a data-loading utility for the project. It is responsible for loading three key DataFrames from Parquet files: _playtime_genre, users_reviews, and df_games_.

**Content:**
- Imports the necessary library (pandas) for working with DataFrames.
- Loads the datasets from Parquet files using pd.read_parquet.

**Relation to Others:**

**data.py** establishes a crucial link by providing access to the game-related data stored in DataFrames. These DataFrames are then used in various API functions.


## functions.py
   
**Purpose:** 
This module contains the core functionality of the API. It defines various functions that perform specific queries on the game datasets. It uses the DataFrames loaded in data.py.

**Content:**
- Imports essential libraries and models (joblib, sklearn).
- Defines functions like PlayTimeGenre, UserForGenre, UsersRecommend, etc., each targeting a specific type of query.
  
**Relation to Others:**
**functions.py** relies on the loaded DataFrames _(playtime_genre, users_reviews, df_games)_ to perform data manipulations and computations. It also imports the pre-trained recommendation model from _recommendation_model.joblib_.

## main.py

**Purpose:** 

This is the main FastAPI application file. It defines the API endpoints and their corresponding functions from functions.py. It establishes the connection between incoming HTTP requests and the API functions.

**Content:**

- Imports FastAPI, HTTPException, and the API functions from functions.py.
- Defines the root endpoint ("/") and various API endpoints like /playtime_genre/{genre}, /user_for_genre/{genre}, etc.

**Relation to Others:**

**main.py** serves as the entry point for handling HTTP requests. It calls the appropriate functions from _functions.py_ based on the requested API endpoint. Additionally, it imports the API functions, which, in turn, rely on the data loaded in _data.py_.

## Overall Flow:

In summary, **data.py** loads the data, **functions.py** processes the data and defines API functionality, and **main.py** orchestrates the API endpoints, connecting HTTP requests to the appropriate functions for data retrieval and manipulation.

The modularity achieved by separating components into different files contributes to a more maintainable, readable, and scalable codebase. It promotes collaboration among team members and facilitates the reuse of code, ultimately enhancing the overall development and maintenance process.

# API Functions

1. _`PlayTimeGenre`_
/playtime_genre/{genre}

  _Finds the year with the most hours played for a specific genre._

2. _`UserForGenre`_
/user_for_genre/{genre}

  _Finds the user with the most hours played for a specific genre._

3. _`UsersRecommend`_
/users_recommend/{year}

  _Identifies the top 3 recommended games for a given year._

4. _`UsersWorstDeveloper`_
/users_worst_developer/{year}

  _Identifies the top 3 developers with the least recommended games for a given year._

5. _`SentimentAnalysis`_
/sentiment_analysis/{developer_company}

  _Counts the number of negative, neutral, and positive reviews for a specified developer._

6. _`GameRecommendations`_
/game_recommendations/{item_id}

  _Provides recommendations for games similar to a given game based on a K-nearest neighbors approach._


# Setting Up Render

1. Go to [Render](https://render.com/) and connect to your GitHub or create an account.

2. In the **dashboard**, click on _"New"_ and create a web service.

3. Fill out the necessary fields.


### General Section

**Name** _Select a name for your web service._

**Region** _Choose the region where your web service runs._

**Instance Type** _Free 0.1 CPU 512 MB (Upgrade according to your needs)._


### Build & Deploy Section

**Repository** _`Paste your repository URL`_

**Branch** `Master.`

**Root Directory** _(Optional)_: _`./(subfolder)`_

**Runtime** _`Python 3`_

**Build Command** _`$ pip install -r requirements.txt`_

**Start Command** _`$ uvicorn main:app --host 0.0.0.0 --port 10000`_


4. Deploy your web service.

5. Find your API ready for consumption by locating the link provided by **Render** within the upper left section of your dashboard after deployment.
