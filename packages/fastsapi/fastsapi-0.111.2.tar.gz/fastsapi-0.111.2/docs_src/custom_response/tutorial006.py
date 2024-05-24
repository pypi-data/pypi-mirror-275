from fastsapi import FastAPI
from fastsapi.responses import RedirectResponse

app = FastAPI()


@app.get("/typer")
async def redirect_typer():
    return RedirectResponse("https://typer.tiangolo.com")
