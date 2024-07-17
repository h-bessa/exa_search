from fastapi import FastAPI

from api.database import init_db
from api.routers import users, history

app = FastAPI()

app.include_router(users.router, prefix="", tags=["users"])
app.include_router(history.router, prefix="", tags=["history"])



@app.on_event("startup")
def on_startup():
    init_db()


@app.get('/')
def read_root():
    return {"Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
