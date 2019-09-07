from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response

app = Starlette()


@app.route("/ping")
async def ping(request: Request) -> Response:
    return PlainTextResponse("pong")
