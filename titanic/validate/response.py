from marshmallow import Schema, fields


class ResponseSchema(Schema):
    """
    Base schema for all responses.
    """
    request_id = fields.Str(required=True)


class TitanicModelNestedPredictionSchema(Schema):
    passenger_id = fields.Str(required=True)
    score = fields.Float(required=True)


class TitanicModelResponseSchema(ResponseSchema):
    """
    Schema for all responses from the titanic_model endpoint.
    """
    prediction = fields.List(
        fields.Nested(
            TitanicModelNestedPredictionSchema,
            required=True
        ),
        required=True
    )


titanic_model_response_schema = TitanicModelResponseSchema()
