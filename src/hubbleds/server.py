from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from solara.server import settings
from starlette.middleware.sessions import SessionMiddleware

import solara.server.starlette


def root(request: Request):
    return JSONResponse({"framework": "solara"})


routes = [
    # Route("/", endpoint=root),
    Mount("/hubbles-law", routes=solara.server.starlette.routes),
    # Mount("/", routes=solara.server.starlette.routes),
]

app = Starlette(routes=routes)

from solara_enterprise.auth.starlette import oauth

# TODO: `secret_key` defined here is for TESTING ONLY
app.add_middleware(
    SessionMiddleware,
    secret_key="some-secret-key",
    max_age=None,
)
