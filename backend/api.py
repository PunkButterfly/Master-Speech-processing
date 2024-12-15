import os
import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import FileResponse

from voicer import Voicer


BACKEND_PORT = int(os.getenv('BACKEND_PORT'))

app = FastAPI()
voicer = Voicer()

@app.post("/voice/")
async def voice(request: Request):
    request_data = await request.json()
    text = request_data["text"]

    file_name = voicer.predict(text)
    return FileResponse(file_name, media_type="audio/mpeg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=BACKEND_PORT)
