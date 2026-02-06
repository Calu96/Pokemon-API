import requests
from typing import Any

class PokemonTimeOut(Exception):
    pass
url="https://pokeapi.co/api/v2/pokemon/"

def fetch_pokemon(pokemon_id:int|str) -> dict[str,Any]:
    in_put=str(pokemon_id).strip().lower()
    URL=f"{url}{in_put}/"
    try:
        response=requests.get(URL,timeout=15)
        response.raise_for_status()
        row=response.json()
        return row
    except requests.exceptions.Timeout as e:
        raise PokemonTimeOut(f"Timed out while fetching pokemon {pokemon_id}") from e
    except requests.exceptions.HTTPError as e:
        status=e.response.status_code if e.response is not None else None
        if status==404:
            raise ValueError(f"Pokemon not found") from e
        raise PokemonTimeOut(f"Error HTTP {status}") from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error consultando PokeAPI") from e

def normalizar_pokemon(row:dict)->dict[str,Any]:
    pokemon_types=[t["type"]["name"] for t in row.get("types",[])]
    pokemon_stats={state["stat"]["name"]:state.get("base_stat") for state in row.get("stats",[])}

    return {"id":row.get("id"),
            "name":row.get("name"),
            "types": pokemon_types,
            "stats": pokemon_stats}

def output_pokemon(pokemon_id:int|str)->dict[str,Any]:
    row=fetch_pokemon(pokemon_id)
    return normalizar_pokemon(row)


