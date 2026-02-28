from fastapi import APIRouter, HTTPException
import os
import random

router = APIRouter()

# Simulating a database
JOKES = [
    {"id": 1, "joke": "Why do programmers prefer dark mode? Because light attracts bugs."},
    {"id": 2, "joke": "How many programmers does it take to change a light bulb? None, that's a hardware problem."},
    {"id": 3, "joke": "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?'"},
    {"id": 4, "joke": "Why did the developer go broke? Because he used up all his cache."},
]

@router.get("/list")
async def list_jokes():
    """Returns all jokes as JSON."""
    return {"count": len(JOKES), "jokes": JOKES}

@router.get("/random")
async def random_joke():
    """Returns a random joke as JSON."""
    return random.choice(JOKES)

@router.get("/info")
async def app_info():
    """
    Returns app environment info. 
    Useful for testing K8s ConfigMaps and Secrets injection.
    """
    return {
        "app_name": "K8s Joke API",
        "version": "1.0.0",
        "environment": os.getenv("APP_ENV", "development"),
        "debug_mode": os.getenv("DEBUG_MODE", "false")
    }
