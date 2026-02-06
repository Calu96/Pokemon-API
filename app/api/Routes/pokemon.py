from fastapi import APIRouter
from app.schemas.pokemon import PokemonOut
router_pokemon = APIRouter()

@router_pokemon.get("/pokemon/{name_id}",response_model=PokemonOut)
def get_pokemon(name_id:str|int):