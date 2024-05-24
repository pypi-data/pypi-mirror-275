from typing import List, Union

from fastsapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[Union[List[str], None], Query()] = None):
    query_items = {"q": q}
    return query_items
