from fastapi import FastAPI

from enum import Enum

class Available(str,Enum):
     ball = "ball"
     bat = "bat"
     solo = "solo"

app = FastAPI()

games = {
     "ball" : ['BasketBall','Football'],
     "bat" : ['Cricket','Badminton'],
     "solo" : ['Gymnastics','Athletics']
}

available = games.keys()
@app.get("/{game}")
async def load(game : Available):
        if game:
            return f"{game.value} are the games that are available"
        else:
            return f"{game} games are not found"