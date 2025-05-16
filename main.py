from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Query
import httpx
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser les requêtes depuis le frontend (Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Remplace "*" par ton domaine exact en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STEAM_API_KEY = os.getenv("STEAM_API_KEY")

@app.get("/steam/achievements")
async def get_achievements(steamid: str = Query(...), appid: str = Query(...)):
    url = "https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/"
    params = {
        "key": STEAM_API_KEY,
        "steamid": steamid,
        "appid": appid
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()
