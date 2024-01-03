<h1 align=center>SteamGames ML OPS</h1>

SteamGames ML OPS is one of the final integrative projects of the Henry Data-Science Bootcamp. The project revolves around the SteamGames datasets, which cover information about games, users and developers from the Steam platform. The main goal of this project was to transform the raw data into a clean, well-organized and optimized format. Subsequently, the data was analyzed and used to train a machine learning model for a recommendation system and to be consumed according to specific queries as endpoints of an API.

Here you can access my [Steam Games Querys API](https://steam-games-querys.onrender.com)

# Directory Details

- **API/** Contains files related to the implementation of API endpoints for data consumption. For a detailed description of the API and its implementation, please refer to the [API README](https://github.com/pono33/SteamGames_ML_OPS/blob/master/API/README.md).

- **datasets/**
  _The datasets folder is divided into two subfolders_

   **processed/**

    **games.parquet:** Processed data about games.

    **items.parquet:** Processed data about items.

    **reviews.parquet:** Processed data about reviews.

    **users.parquet:** Processed data about users.


   **raw/**

    **Diccionario de Datos STEAM.xlsx:** Steam dataset dictionary.

    **steam_games.json.gz:** Raw data about Steam games.

    **user_reviews.json.gz:** Raw data about user reviews.

    **users_items.json.gz:** Raw data about user items.

_The raw subfolder includes the Steam datasets provided by Henry for analysis, while the processed subfolder contains the resulting dataframes after the ETL (Extract, Transform, Load) process._

- **.gitignore:** File to specify untracked files and directories that Git should ignore.

- **EDA.ipynb:** Jupyter Notebook for Exploratory Data Analysis.

- **ETL.ipynb:** Jupyter Notebook for the Extract, Transform, Load (ETL) process.

- **ML_Model.ipynb:** Jupyter Notebook for developing the machine learning model.

- **requirements.txt:** File specifying project dependencies.

# ETL Process: 

This ETL (Extract, Transform, Load) script focuses on processing and transforming the raw data, performing sentiment analysis and web-scrapping. The process is divided into three main sections: **User_Reviews**, **User_items** and **Games**.

## User Reviews and Sentiment Analysis

#### Extract

The raw user reviews data is loaded from the compressed JSON file ('user_reviews.json.gz'). The file is read line by line, and each line is converted from a JSON string to a Python dictionary using `ast.literal_eval`. The resulting dictionaries are stored in a list, and a DataFrame is created from this list.

#### Transform

1. The 'reviews' column is exploded to create a new DataFrame, `reviews_df`, expanding the nested structure.
2. The 'user_id' column is concatenated with `reviews_df` to form the final processed DataFrame, `df_reviews`.
3. Duplicate rows are removed, and non-relevant columns ('funny', 'last_edited', 'helpful', 0) are dropped.
4. Records with at least one null value are identified and displayed for review.
5. Records with null values in all specific columns ('posted', 'item_id', 'recommend', 'review') are dropped.
6. The 'posted' column is converted to a string data type.
7. The 'item_id' column is converted to an integer data type.
8. The 'recommend' column is converted to a boolean data type.
9. A new column, 'year_posted,' is created by extracting the year from the 'posted' column.
10. Missing values in 'year_posted' are filled using the mean year calculated for each 'item_id' and the overall mean.
11. The 'year_posted' column is converted to integer values.
12. The original 'posted' column is dropped.

### sentiment_analysis

1. Sentiment analysis is conducted on the 'review' column using the TextBlob library.
2. A new column, 'sentiment_analysis,' is created to store sentiment scores (0 for negative, 1 for neutral, 2 for positive).
3. The original 'review' column is dropped.

### Load

The final processed DataFrame from the **User_Reviews** section is exported re exported to the 'datasets/processed' directory in Parquet format for further analysis.


## User Items

This section of the ETL process focuses on handling the raw user/items data. The script extracts, transforms, and loads the data to create two processed datasets: `users.parquet` and `items.parquet`.

### Extract

The raw user items data is loaded from the compressed JSON file ('users_items.json.gz'). Each line is converted to a dictionary using `ast.literal_eval`, and the resulting dictionaries are stored in a list.

### Transform

1. A DataFrame, `df_users_items`, is created from the list of dictionaries.
2. The 'steam_id' column is converted to integers.
3. Duplicate rows based on all columns except the last one are removed.
4. Records where 'items_count' is '0' (users who don't own any games) are filtered and removed.
5. The 'items' column, which contains lists of dictionaries, is transformed into a separate DataFrame, `df_items`.
6. The 'user_id' column is replicated according to the 'items_count' value.
7. The 'user_id_replicated' column is added to the 'df_items' DataFrame.
8. The 'item_id' column is converted to integers.
9. Columns are renamed for clarity.
10. Unnecessary columns ('playtime_2weeks') are removed from the 'df_items' DataFrame.
11. The 'items' column is dropped from the `df_users_items` DataFrame.

The `df_users` DataFrame provides information about users, including their unique identifier, the count of items they own, Steam identifier, and associated user URL. On the other hand, the `df_items` DataFrame contains details about the items, such as the associated user identifier, unique item identifier, item name, and playtime in minutes.

### Load

Two processed datasets, `users.parquet` and `items.parquet`, are exported to the 'datasets/processed' directory in Parquet format.


## Games

This section of the ETL process is dedicated to handling the raw games data. The script extracts, transforms, and loads the data to create a processed dataset named `games.parquet`.

### Extract

The raw games data is loaded from the compressed JSON file ('steam_games.json.gz'). Each line, representing a game, is converted from a JSON string to a Python dictionary using the `json.loads` function. The resulting dictionaries are stored in a list, `games_row`.

### Transform

1. A DataFrame, `df_games`, is created from the list of dictionaries.
2. Rows with all missing values are dropped.
3. The 'release_date' column is converted to datetime format, and the 'release_year' column is extracted.
4. Unnecessary columns ('specs', 'early_access', 'price') are removed.
5. Missing values in 'title', 'developer', 'genre' and 'release_year' are filled using web scraping with a custom `WebScraper` class.
7. Missing values in 'developer' are imputed with values from 'publisher'.
8. Missing values in 'title' are imputed with values from 'app_name'.
9. Missing the most relevant values in 'genres' are imputed with values from 'tags'.
10. Rows with missing values in the 'id' column are removed.
11. Missing values in 'genres' are imputed with the string 'unknown'.
12. Missing values in 'developer' are imputed with the string 'unknown'.
13. Missing values in 'release_year' are imputed with the rounded mean of existing values.
14. The most relevant genre for each record is determined based on genre frequency distribution.
15. Columns are renamed for clarity.
16. The 'item_id' column is converted to integers.
17. The 'release_year' column is converted to integers.

### Load

The processed dataset, `games.parquet`, is exported to the 'datasets/processed' directory in Parquet format.

# EDA Process

This exploratory data analysis (EDA) focuses on the datasets resulting from the ETL process: games.parquet, items.parquet, reviews.parquet, and user.parquet. The primary goal is to identify key features for the development of a games recommendation model. Subsequently, the analysis involves merging necessary features from different datasets and optimizing object types to enhance memory usage efficiency. The end objective is to deploy a RESTful API  housing all necessary data for both powering the recommendation model and facilitating specific queries to the datasets.

Overall, the EDA script meticulously addresses each dataset, employing systematic techniques to optimize memory usage while retaining crucial information. More detailed analysis description in the EDA script

# Game Recommendation System

## Overview
The **ML_Model.py** script implements a game recommendation system using machine learning techniques. It is designed to provide users with game recommendations similar to a specified game, employing a K-nearest neighbors approach after transforming the input data.

## Implementation Details
The script is divided into several key sections:

**1. Importing Libraries**

The required libraries for the project are imported, including Pandas for data manipulation, Scikit-learn for machine learning tools, and Joblib for model persistence.

**2. Importing Games Dataset**

The script reads the processed games dataset and performs initial data preprocessing, including dropping unnecessary columns and optimizing data types for memory efficiency.

**3. Exporting API Dataset**

The preprocessed games dataset is exported in Parquet format for use in the API.

**4. TF-IDF Vectorization**

The script creates TF-IDF vectorizers for the 'developer,' 'genre,' and 'tags' columns, along with a transformer for the 'release_year' column. These components are combined using Scikit-learn's ColumnTransformer.

**5. Creating KNN Model**

A K-nearest neighbors model is created using the cosine distance metric and a brute-force algorithm.

**6. Creating Preprocessing and KNN Model Pipeline**

The TF-IDF vectorizers and KNN model are combined into a Scikit-learn pipeline for ease of use.

**7. Fitting Pipeline to the DataFrame**

The pipeline is fitted to the preprocessed games DataFrame.

**8. Saving Model**

The trained pipeline is saved using Joblib for later use in the API.

**9. Function to Get Recommendations**

A function, game_recommendations, is defined to provide game recommendations based on a specified game (item_id) using the K-nearest neighbors approach.

**10. Application Example**

An example is provided to demonstrate how to use the recommendation function with a specific item_id, resulting in a list of recommended titles.

## Usage

**To use the recommendation system:**

- Ensure that the required libraries are installed (see requierements.txt).
- Run the script in a Jupyter notebook or Python environment.
- Utilize the game_recommendations function with a specific item_id to get recommendations.
  
## Function Parameters
**item_id:** A 6-digit integer representing the game for which recommendations are sought.

**Application example**
```
game_recommendations(643980)
```

This will output a list of 5 recommended titles similar to the specified game.
```
[{'1': 'Brief Karate Foolish'},
 {'2': 'Nightside Demo'},
 {'3': "Defender's Quest: Valley of the Forgotten (DX edition)"},
 {'4': 'Labyrinth - Starter Pack'},
 {'5': 'MINDNIGHT'}]
```

**Notes:**

The script assumes a Jupyter environment for execution.

The dataset path and other configurations can be adjusted as needed.

Feel free to explore and adapt the script to meet your specific requirements.


