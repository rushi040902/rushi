from fastapi import FastAPI

from user.api import UserAPI

app=FastAPI()
app.include_router(UserAPI.router)

