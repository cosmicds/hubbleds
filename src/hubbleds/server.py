from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from solara.server import settings

import solara.server.starlette


def root(request: Request):
    return JSONResponse({"framework": "solara"})


routes = [
    # Route("/", endpoint=root),
    Mount("/", routes=solara.server.starlette.routes),
]

app = Starlette(routes=routes)
