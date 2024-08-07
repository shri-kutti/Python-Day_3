from fastapi import FastAPI,Path

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
champions  = {
     1: {
          "name" : "Bravo",
          "class" : "xi",
          "gen" : "y"
     },
     2: {
          "name" : "Limano",
          "class" : "xi",
          "gen" : "x"
     }
}

available = games.keys()
@app.get("/{game}")
async def load(game : Available):
        if game:
            return f"{game.value} are the games that are available"
        else:
            return f"{game} games are not found"

#using path parameters 
''' functionalities include 1.setting a default constraint num : int
     2.title and description to show on api documentation or schema
     3.constraints : ge,le,lt,gt = 0123
     4.regex = "^[a-zA-Z0-9_]+$" '''
@app.get("/players/{num}")
def players(num : int = Path(title="Champios",description="The Id of the player u wanna retrive: ",lt=10)): #none was initially set as default value but didn't work
     return champions[num]

@app.get("/getbyname")  #url looks like g...com/getbyname?search=john ...
def get_by_name(name : str):
     for i in champions:
          if champions[i]["name"] == name:
               return champions[i]
          else:
               return "U are not registered"