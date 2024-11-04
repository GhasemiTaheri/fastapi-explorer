from fastapi import FastAPI
from web import creature, explorer, game, user
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(game.router)
app.include_router(user.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
