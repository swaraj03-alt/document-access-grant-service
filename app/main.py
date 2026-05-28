from fastapi import FastAPI

from app.api.grants import router as grant_router

app = FastAPI()

app.include_router(grant_router)


@app.get("/")
async def root():
    return {"message": "Grant Service Running"}