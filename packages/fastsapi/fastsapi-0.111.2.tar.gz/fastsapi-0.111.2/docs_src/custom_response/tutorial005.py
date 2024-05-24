from fastsapi import FastAPI
from fastsapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Hello World"
