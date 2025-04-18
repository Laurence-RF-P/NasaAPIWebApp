from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from routers import space_fact, asteroids

app = FastAPI(title="Space Dashboard 🚀")

app.include_router(space_fact.router, prefix="/api")
app.include_router(asteroids.router, prefix="/api")

app.mount("/", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    file_path = Path(__file__).parent / "static" / "index.html"
    return FileResponse(file_path)
