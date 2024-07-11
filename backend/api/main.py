from fastapi import FastAPI

from api.routers import users

app = FastAPI()

app.include_router(users.router, prefix="/api/v1", tags=["users"])


@app.get('/')
def read_root():
    return {"Hello World"}
