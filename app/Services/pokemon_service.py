from typing import Any
from app.schemas.pokemon import PokemonOut
from app.Clientes.pokeapi_client import fetch_pokemon

def normalizar_pokemon(row:dict)->dict[str,Any]:
    pokemon_types=[t["type"]["name"] for t in row.get("types",[])]
    pokemon_stats={state["stat"]["name"]:state.get("base_stat") for state in row.get("stats",[])}

    return {"id":row.get("id"),
            "name":row.get("name"),
            "types": pokemon_types,
            "stats": pokemon_stats}

def output_pokemon(pokemon_id:int|str)->PokemonOut:
    raw=normalizar_pokemon(fetch_pokemon(pokemon_id))
    return PokemonOut(id=raw["id"],name=raw["name"],types=raw["types"],stats=raw["stats"])

print(output_pokemon("charizard"))






