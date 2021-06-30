from fastapi import APIRouter
from shared import bikecalc

router = APIRouter()

@router.get("/calculate/gear_ratios")
async def calculate_gear_ratios(
        min_chainring: int = 36,
        max_chainring: int = 50,
        min_cog: int = 14,
        max_cog: int = 28):
    """Calculates a hierarchy of gear ratios from cogs to chainrings.

    Default values are from my bike."""
    return bikecalc.calculate_gear_ratios(min_chainring, max_chainring, min_cog, max_cog)

def init_app(app):
    app.include_router(router)

