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
        raw=response.json()
        return raw
    except requests.exceptions.Timeout as e:
        raise PokemonTimeOut(f"Timed out while fetching pokemon {pokemon_id}") from e
    except requests.exceptions.HTTPError as e:
        status=e.response.status_code if e.response is not None else None
        if status==404:
            raise ValueError(f"Pokemon not found") from e
        raise PokemonTimeOut(f"Error HTTP {status}") from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error consultando PokeAPI") from e