from fastapi import FastAPI
from api.Routes.health import router_pokemon as health_router
from api.Routes.health import router_pokemon as pokemon_router
from api.Routes.compare import router_pokemon as compare_router

def create_app() -> FastAPI:
    app = FastAPI(title="Pokemon API",version="0.1.0")
    app.include_router(health_router,prefix="/api/v1",tags=["health"])
    app.include_router(pokemon_router,prefix="/api/v1",tags=["pokemon"])
    app.include_router(compare_router,prefix="/api/v1",tags=["compare"])
    return app

app = create_app()

