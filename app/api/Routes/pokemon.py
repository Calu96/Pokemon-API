from fastapi import APIRouter,HTTPException
from app.schemas.pokemon import PokemonOut
from app.Services.pokemon_service import output_pokemon as output_pokemon
from app.Clientes.pokeapi_client import PokemonTimeOut
router_pokemon = APIRouter()

@router_pokemon.get("/pokemon/{name_id}",response_model=PokemonOut)
def get_pokemon(name_id:str):
    try:
        return output_pokemon(name_id)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=400,detail=str(e))
    except PokemonTimeOut as e:
        raise HTTPException(status_code=400,detail=str(e))
