from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from app.routers import jokes
import os

# Initialize App
app = FastAPI(title="K8s Joke API")

# Setup Templates
templates = Jinja2Templates(directory="app/templates")

# Include Routers
app.include_router(jokes.router, prefix="/jokes", tags=["Jokes"])

# Custom 404 Exception Handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    # Return HTML for browser, JSON for API clients (curl)
    accept_header = request.headers.get("accept", "")
    if "text/html" in accept_header:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    return JSONResponse(content={"error": "Not Found", "detail": "The requested resource does not exist"}, status_code=404)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health_check():
    """
    Critical for Kubernetes Liveness and Readiness Probes.
    Returns 200 OK if the app is running.
    """
    return {"status": "healthy", "pod_name": os.getenv("HOSTNAME", "unknown")}
