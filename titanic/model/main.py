import random
from typing import NamedTuple


class ModelInput(NamedTuple):
    """
    Data for calculating the probability of survival of the passengers
    """
    sex: str
    parch: int
    sib_sp: int
    fare: float
    embarked: str
    p_class: str


def predict_survival_prop(model_input: ModelInput) -> float:
    """
    Calculate the probability of survival of the passengers
    """
    return random.random()
