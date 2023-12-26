from fastapi import FastAPI
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
                p {
                    color: #666;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Steam Platform Game Query API</h1>
            <p>This tool that can be used by game developers to improve their games, by game publishers to track their sales, and by gamers to find new games to play.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=template)

# API endpoints

@app.get("/playtime_genre/{genero}")
def read_playtime_genre(genero: str):
    try:
        result = PlayTimeGenre(genero)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/user_for_genre/{genero}")
def read_user_for_genre(genero: str):
    try:
        result = UserForGenre(genero)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users_recommend/{año}")
def read_users_recommend(año: int):
    try:
        result = UsersRecommend(año)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users_worst_developer/{año}")
def read_users_worst_developer(año: int):
    try:
        result = UsersWorstDeveloper(año)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/sentiment_analysis/{empresa_desarrolladora}")
def read_sentiment_analysis(empresa_desarrolladora: str):
    try:
        result = sentiment_analysis(empresa_desarrolladora)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/game_recommendations/{item_id}")
def read_game_recommendations(item_id: int):
    try:
        result = game_recommendations(item_id)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))