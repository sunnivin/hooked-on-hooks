from pydantic import validate_argument, Field, Strict
from typing_extensions import Annotated, Union

from typing import Any 

@validate_argument # type: ignore
def foo(bar: Union[str, Annotated[int, Field(ge=0, multiple_of=1)]],int_variable: Annotated[int,str]) -> Union[Any,int]:

    print(f"Argument types {type(bar),type(int_variable)}")
    print(f"Argument values {bar,int_variable}")
    print("ok")

    return bar


print(f"With string as int:\n {foo('hi',int_variable='20')}")
print(f"With int as input: \n {foo(4,int_variable=20)}")
# Uncommenting this will fail print(f"String input: {foo('hi',int_variable='yes')}")