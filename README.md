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

### User Reviews and Sentiment Analysis

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

The final processed DataFrame from the **User_Reviews** section is exported in Parquet format for further analysis.



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


