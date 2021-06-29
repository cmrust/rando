from fastapi import FastAPI
from shared import bikecalc
from models import db

def load_app():
    app = FastAPI(title="Rando Server")
    db.init_app(app)
    return app

app = load_app()

@app.get("/")
async def root():
    return {"message": "Hello World2"}

@app.get("/bicycles/{bicycle_id}")
async def read_bicycle(bicycle_id: int):
    return {"bicycle_id": bicycle_id}


@app.get("/calculate/gear_ratios")
async def calculate_gear_ratios(min_chainring: int = 36, max_chainring: int = 50, min_cog: int = 14, max_cog: int = 28):
    """Calculates a hierarchy of gear ratios from cogs to chainrings.

    Default values are from my bike."""
    return bikecalc.calculate_gear_ratios(min_chainring, max_chainring, min_cog, max_cog)



from pydantic import BaseModel

from models.users import User

@app.get("/users/{uid}")
async def get_user(uid: int):
    user = await User.get_or_404(uid)
    return user.to_dict()

class UserModel(BaseModel):
    name: str

@app.post("/users")
async def add_user(user: UserModel):
    rv = await User.create(nickname=user.name)
    return rv.to_dict()

@app.delete("/users/{uid}")
async def delete_user(uid: int):
    user = await User.get_or_404(uid)
    await user.delete()
    return dict(id=uid)
