from fastapi import FastAPI, Path, HTTPException
from enum import Enum

class Available(str, Enum):
    ball = "ball"
    bat = "bat"
    solo = "solo"

app = FastAPI()

games = {
    "ball": ['BasketBall', 'Football'],
    "bat": ['Cricket', 'Badminton'],
    "solo": ['Gymnastics', 'Athletics']
}

champions = {
    1: {
        "name": "Bravo",
        "class": "xi",
        "gen": "y"
    },
    2: {
        "name": "Limano",
        "class": "xi",
        "gen": "x"
    }
}

@app.get("/{game}")
async def load(game: Available):
    if game.value in games:
        return {game.value: games[game.value]}
    else:
        raise HTTPException(status_code=404, detail="Game not found")

@app.get("/players/{num}")
def players(num: int = Path(title="Champions", description="The ID of the player you want to retrieve", ge=1, le=10)):
    if num in champions:
        return champions[num]
    else:
        raise HTTPException(status_code=404, detail="Player not found")

@app.get("/getbyname")
def get_by_name(name: str):
    for player in champions.values():
        if player["name"] == name:
            return player
    raise HTTPException(status_code=404, detail="Player not found")
