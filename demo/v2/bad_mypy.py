# pip install pydantic
from pydantic import TypeAdapter, field_validator
from typing_extensions import NotRequired, TypedDict


class Item(TypedDict):
    id: int
    price: float
    description: NotRequired[str]

    @field_validator("price", mode="before")
    def check_non_zero(cls, v):
        if v <= 0:
            raise ValueError("price cannot be zero")
        else:
            return v


if __name__ == "__main__":
    ItemsTypeAdapter: TypeAdapter[list[Item]] = TypeAdapter(list[Item])
    sample_data = [
        {"id": 1, "price": 10.0, "description": "A nice item"},
        {"id": 2, "price": 20.0, "description": "Another nice item"},
        {"id": 3, "price": 0.0, "description": "A bad item"},
    ]
    try:
        items = ItemsTypeAdapter.validate_python(sample_data)
        from pprint import pprint
        pprint(items, sort_dicts=False)
    except ValueError as e:
        print(e)