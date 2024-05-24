from fastsapi import FastAPI
from fastsapi.responses import RedirectResponse

app = FastAPI()


@app.get("/fastapi", response_class=RedirectResponse)
async def redirect_fastapi():
    return "https://fastapi.tiangolo.com"
