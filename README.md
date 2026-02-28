# K8s Joke API

A simple FastAPI project designed to test Kubernetes concepts.

## Features
- **JSON API**: Returns jokes.
- **HTML Responses**: Serves simple HTML for browser testing.
- **Health Check**: `/health` endpoint. 
- **ConfigMap Ready**: Reads `APP_ENV` and `DEBUG_MODE` from environment variables.
- **Custom 404**: Handles missing routes gracefully.

## Local Development

**Install dependencies**:
```bash
   pip install -r requirements.txt
```
## Endpoints

```bash
# index page
curl localhost:8000/

# random joke
curl localhost:8000/jokes/random

# all jokes
curl localhost:8000/jokes/list

# health check probe
curl localhost:8000/health

# check env
curl localhost:8000/jokes/info

# 404 handler
curl localhost:8000/wtf
```
## Objective

Implement and understand the concept of kubernetes cluster.

## Docs

Find the docs at [/docs](https://github.com/DevOpsByNavin/k8s-svc/tree/main/docs) to get more idea on k8s services.
