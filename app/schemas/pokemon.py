from pydantic import BaseModel,Field

class PokemonOut(BaseModel):
    id: int = Field(...,gt=0)
    name: str = Field(...,min_length=1,max_length=50)
    types:list[str]= Field(...)
    stats:dict[str,int]= Field(...)
class NamedAPIResource(BaseModel):
    name: str
    url: str
class PokememonListOut(BaseModel):
    count:int
    next:str|None
    prev:str|None
    results:list[NamedAPIResource]