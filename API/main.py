from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowAuthorizationCode

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
            <!-- Swagger UI -->
            <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@3.49.0/swagger-ui.css" />
            <!-- ReDoc -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/redoc@next/dist/redoc.min.css" />
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
                #swagger-ui {
                    display: none;
                }
                #redoc {
                    display: none;
                }
                #toggle-buttons {
                    text-align: center;
                    margin-top: 20px;
                }
                #toggle-buttons button {
                    margin: 5px;
                    padding: 10px;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <h1>Steam Platform Game Query API</h1>
            <p>This tool can be used by game developers to improve their games, by game publishers to track their sales, and by gamers to find new games to play.</p>
            <div id="toggle-buttons">
                <button onclick="showSwaggerUI()">Swagger UI</button>
                <button onclick="showReDoc()">ReDoc</button>
            </div>
            <!-- Swagger UI container -->
            <div id="swagger-ui"></div>
            <!-- ReDoc container -->
            <div id="redoc"></div>

            <script src="https://unpkg.com/swagger-ui-dist@3.49.0/swagger-ui-bundle.js"></script>
            <script src="https://unpkg.com/swagger-ui-dist@3.49.0/swagger-ui-standalone-preset.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/redoc@next/dist/redoc.min.js"></script>
            <script>
                function showSwaggerUI() {
                    document.getElementById("swagger-ui").style.display = "block";
                    document.getElementById("redoc").style.display = "none";
                    initSwaggerUI();
                }

                function showReDoc() {
                    document.getElementById("swagger-ui").style.display = "none";
                    document.getElementById("redoc").style.display = "block";
                    initReDoc();
                }

                function initSwaggerUI() {
                    const ui = SwaggerUIBundle({
                        url: "/docs/openapi.json",
                        dom_id: '#swagger-ui',
                        presets: [
                            SwaggerUIBundle.presets.apis,
                            SwaggerUIStandalonePreset
                        ],
                        layout: "BaseLayout"
                    });
                }

                function initReDoc() {
                    const ui = Redoc({
                        specUrl: "/docs/openapi.json",
                        dom_id: '#redoc',
                        pathInMiddlePanel: true,
                    });
                }

                // Show Swagger UI by default
                showSwaggerUI();
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=template)


# API endpoints:

@app.get("/playtime_genre/{genre}")
async def read_playtime_genre(genre: str):
    try:
        result = PlayTimeGenre(genre)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/user_for_genre/{genre}")
async def read_user_for_genre(genre: str):
    try:
        result = UserForGenre(genre)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users_recommend/{year}")
async def read_users_recommend(year: int):
    try:
        result = UsersRecommend(year)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users_worst_developer/{year}")
async def read_users_worst_developer(year: int):
    try:
        result = UsersWorstDeveloper(year)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/sentiment_analysis/{developer_company}")
async def read_sentiment_analysis(developer_company: str):
    try:
        result = sentiment_analysis(developer_company)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/game_recommendations/{item_id}")
async def read_game_recommendations(item_id: int):
    try:
        result = game_recommendations(item_id)
        return result
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
