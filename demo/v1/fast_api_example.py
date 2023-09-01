from typing import Any
from fastapi import FastAPI, status
from pydantic import BaseModel, ValidationError, conint, Field, confloat


app = FastAPI()


class Model(BaseModel):
    list_of_ints: list[int] = Field(description="A list of ints", le=42,min_items=3)
    list_of_floats: list[float] = Field(description="A list of floats", ge=42.6,le=44)
    an_int: int = Field(description="A single int", le=5)


@app.post("/validation", status_code=status.HTTP_201_CREATED, tags=["validate"])
def validate_input(model_in: Model) -> dict[Any,Any] :
    return {"msg": True}

data : dict[Any,Any] = dict(
    list_of_ints=[4, 2, 10],
    list_of_floats=[43.5],
    an_int=4
)

try:
    validated = Model(**data)
    print(f"My validated dict: {validated}")
except ValidationError as e:
    print(e)


