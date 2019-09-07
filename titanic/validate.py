from marshmallow import Schema, fields


class RequestSchema(Schema):
    """
    Base schema for all incoming requests to all endpoints.
    """
    request_id = fields.Str(required=True)


class TitanicModelNestedDataSchema(Schema):
    passenger_id = fields.Str(required=True)
    sex = fields.Str(required=True)
    sib_sp = fields.Int(required=True)
    parch = fields.Int(required=True)
    fare = fields.Int(required=True)
    embarked = fields.Str(required=True)
    p_class = fields.Str(required=True)


class TitanicModelRequestSchema(RequestSchema, Schema):
    """
    Schema for all incoming requests to the titanic_model endpoint.
    """
    data = fields.List(
        fields.Nested(
            TitanicModelNestedDataSchema, 
            required=True
        ),
        required=True
    )


titanic_model_request_schema = TitanicModelRequestSchema()
