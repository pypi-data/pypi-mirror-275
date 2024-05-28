# app/routes/ping.py
from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

async def fetch_data(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

@router.get("/ping")
async def get_data():
    url = "https://run.mocky.io/v3/80886e97-47c1-4a7f-b547-77c79498b1cc"
    try:
        data = await fetch_data(url)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
