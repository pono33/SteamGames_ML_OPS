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



