import math
from typing import Annotated, TypeVar, Union

from annotated_types import Gt
from typing_extensions import NotRequired, TypedDict

from pydantic import TypeAdapter
from pydantic.functional_validators import AfterValidator

Number = TypeVar('Number', bound=Union[float, int])


def check_finite(v: Number) -> Number:
    if not math.isfinite(v):
        raise ValueError('Expected a finite number')
    else:
        return v


Positive = Annotated[Number, Gt(0)]
Finite = Annotated[Number, AfterValidator(check_finite)]

class Item(TypedDict):
    id: int
    price: Positive[Finite[float]]
    description: NotRequired[str]


if __name__ == '__main__':
    ItemsTypeAdapter: TypeAdapter[list[Item]] = TypeAdapter(list[Item])
    sample_data = [
        {'id': 1, 'price': 10.0, 'description': 'A nice item'},
        {'id': 2, 'price': 20.0, 'description': 'Another nice item'},
        {'id': 3, 'price': 0.0, 'description': 'A bad item'},
        {'id': 3, 'price': math.nan, 'description': 'Another bad one'},
        {'id': 3, 'price': math.inf, 'description': 'A big bad one'},
    ]
    try:
        items = ItemsTypeAdapter.validate_python(sample_data)
        from pprint import pprint
        pprint(items, sort_dicts=False)
    except ValueError as e:
        print(e)