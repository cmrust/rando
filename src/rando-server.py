from fastapi import FastAPI
from shared import bikecalc
from models import db

from views import users

def load_modules(app=None):
    users.init_app(app)

def load_app():
    app = FastAPI(title="Rando Server")
    db.init_app(app)
    load_modules(app)
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

