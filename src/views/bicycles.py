from fastapi import APIRouter
from pydantic import BaseModel

from models.bicycles import Bicycle

router = APIRouter()

@router.get("/bicycles/{uid}")
async def get_bicycles(uid: int):
    bicycle = await Bicycle.get_or_404(uid)
    return bicycle.to_dict()

class BicycleModel(BaseModel):
    year: int
    make: str
    model: str

@router.post("/bicycles")
async def add_bicycle(bicycle: BicycleModel):
    rv = await Bicycle.create(
        year=bicycle.year,
        make=bicycle.make,
        model=bicycle.model)
    return rv.to_dict()

@router.delete("/bicycles/{uid}")
async def delete_bicycle(uid: int):
    bicycle = await Bicycle.get_or_404(uid)
    await bicycle.delete()
    return dict(id=uid)

def init_app(app):
    app.include_router(router)
