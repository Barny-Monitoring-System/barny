from fastapi import FastAPI
from routes import agents

app = FastAPI()

app.include_router(agents.router)
