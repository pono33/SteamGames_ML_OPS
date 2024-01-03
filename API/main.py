from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

# Import your functions from functions.py
from functions import PlayTimeGenre, UserForGenre, UsersRecommend, UsersWorstDeveloper, sentiment_analysis, game_recommendations

app = FastAPI()

# Index
@app.get("/", response_class=HTMLResponse)
async def index():
    template = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Steam Query API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                }

                li {
                    width: 60%;
                    text-align: center;
                    margin-bottom: 20px;
                    font-family: Arial, sans-serif;
                    font-weight: bold;
                }

                .my-form {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }

                .my-form label {
                    margin-bottom: 7px;
                }

                .my-form .form-inputs {
                    margin-left: auto;
                }

                .my-form input[type="text"],
                .my-form input[type="submit"] {
                    margin-left: auto;
                }

            </style>
        </head>
        <body>
            <h1>Steam Platform Game Query API</h1>
            <ul>
                <li>
                    <form action="/playtime_genre" method="get" class="my-form">
                        <label for="genre">playtime_genre:</label>
                        <input type="text" id="genre" name="genre" required placeholder="Genre">
                        <input type="submit" value="Submit">
                    </form>
                </li>
                <li>
                    <form action="/user_for_genre" method="get" class="my-form">
                        <label for="genre">user_for_genre:</label>
                        <input type="text" id="genre" name="genre" required placeholder="Genre">
                        <input type="submit" value="Submit">
                    </form>
                </li>
                <li>
                    <form action="/users_recommend" method="get" class="my-form">
                        <label for="year">users_recommend:</label>
                        <input type="number" id="year" name="year" required placeholder="Year">
                        <input type="submit" value="Submit">
                    </form>
                </li>
                <li>
                    <form action="/users_worst_developer" method="get" class="my-form">
                        <label for="year">users_worst_developer:</label>
                        <input type="number" id="year" name="year" required placeholder="Year">
                        <input type="submit" value="Submit">
                    </form>
                </li>
                <li>
                    <form action="/sentiment_analysis" method="get" class="my-form">
                        <label for="developer_company">sentiment_analysis:</label>
                        <input type="text" id="developer_company" name="developer_company" required placeholder="Developer Company">
                        <input type="submit" value="Submit">
                    </form>
                </li>
                <li>
                    <form action="/game_recommendations" method="get" class="my-form">
                        <label for="item_id">game_recommendations:</label>
                        <input type="text" id="item_id" name="item_id" required placeholder="Item_id">
                        <input type="submit" value="Submit">
                    </form>
                </li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=template)

# API endpoints

@app.get("/playtime_genre")
async def read_playtime_genre(genre: str):
    try:
        result = PlayTimeGenre(genre)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/user_for_genre")
async def read_user_for_genre(genre: str):
    try:
        result = UserForGenre(genre)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users_recommend")
async def read_users_recommend(year: int):
    try:
        result = UsersRecommend(year)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users_worst_developer")
async def read_users_worst_developer(year: int):
    try:
        result = UsersWorstDeveloper(year)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/sentiment_analysis")
async def read_sentiment_analysis(developer_company: str):
    try:
        result = sentiment_analysis(developer_company)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/game_recommendations")
async def read_game_recommendations(item_id: int):
    try:
        result = game_recommendations(item_id)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
