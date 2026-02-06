from fastapi import APIRouter

router_pokemon = APIRouter()

@router_pokemon.get("/health")
def get_health():
    return {"message": "ok"}