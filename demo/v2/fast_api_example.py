from typing import Any
from fastapi import FastAPI, status
from pydantic import BaseModel, ValidationError, conint, Field, confloat, conlist


app = FastAPI()


class Model(BaseModel):
    list_of_ints: conlist(conint(le=42),min_length=3) = Field(description="A list of ints") # type: ignore 
    list_of_floats: list[confloat(ge=42.6, le=44)] = Field(description="A list of floats") # type: ignore
    an_int: conint(le=5) = Field(description="A single int") # type: ignore

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


