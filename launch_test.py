from pathlib import Path
print("Running launch_test.py from:", Path(__file__).resolve())

from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from pathlib import Path

app = FastAPI()

@app.get("/")
def serve_index():
    path = Path(__file__).parent / "static" / "index.html"
    print(f"📁 Looking for: {path.resolve()}")
    if not path.exists():
        print("🚫 File not found!")
        return PlainTextResponse("index.html NOT FOUND", status_code=404)
    return FileResponse(path)

@app.get("/test")
def test():
    print("/test was called!")
    return {"message": "Hello from /test"}
