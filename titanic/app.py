from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse, Response

from titanic.validate import titanic_model_request_schema

app = Starlette()


@app.route("/ping", methods=['GET'])
async def ping(request: Request) -> Response:
    """
    Ping test endpoint
    """
    return PlainTextResponse("pong")


@app.route("/titanic/model", methods=['POST'])
async def titanic_model(request: Request) -> Response:
    """
    The endpoint returns the probability of survival of the passengers
    on the Titanic based on passenger data.
    """
    request_body = await extract_request(request)
    return JSONResponse(request_body, 201)


async def extract_request(request: Request) -> dict:
    """
    Validate the JSON request and extract the body to Python dict object.
    """
    request_json = await request.json()
    request_body = titanic_model_request_schema.load(request_json)
    return request_body
