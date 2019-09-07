from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse, Response

from titanic.model.main import predict_survival_prop, ModelInput
from titanic.validate.request import titanic_model_request_schema
from titanic.validate.response import titanic_model_response_schema

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
    prediction_output = await predict_survival_probability(
        passenger_data=request_body["data"]
    )
    response_data = titanic_model_response_schema.load({
        "request_id": request_body["request_id"],
        "prediction": prediction_output,
    })
    return JSONResponse(response_data, 201)


async def predict_survival_probability(passenger_data: dict) -> list:
    """
    Prepare model input into desired format
    and call predict_survival_prop function
    """
    prediction_output = []

    for passenger in passenger_data:
        print(passenger)
        model_input = ModelInput(
            sex=passenger["sex"],
            parch=passenger["parch"],
            sib_sp=passenger["sib_sp"],
            fare=passenger["fare"],
            embarked=passenger["embarked"],
            p_class=passenger["p_class"],
        )
        score = predict_survival_prop(model_input)
        prediction_output.append({
            "passenger_id": passenger["passenger_id"],
            "score": score,
        })

    return prediction_output


async def extract_request(request: Request) -> dict:
    """
    Validate the JSON request and extract the body to Python dict object.
    """
    request_json = await request.json()
    request_body = titanic_model_request_schema.load(request_json)
    return request_body
