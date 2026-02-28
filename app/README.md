# K8s Joke API

A simple FastAPI project designed to test Kubernetes concepts.

## Features
- **JSON API**: Returns jokes.
- **HTML Responses**: Serves simple HTML for browser testing.
- **Health Check**: `/health` endpoint. 
- **ConfigMap Ready**: Reads `APP_ENV` and `DEBUG_MODE` from environment variables.
- **Custom 404**: Handles missing routes gracefully.

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
