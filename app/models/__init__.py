import datetime
from dataclasses import field
from typing import Union, Annotated

from pydantic import BaseModel, conint, AfterValidator, typing, computed_field


# class ConverterRequest(BaseModel):
#     number: Union[int, str]


class ConverterResponse(BaseModel):
    arabic: int
    roman: str


def val_adult(value: int) -> bool:
    if value >= 18:
        return True
    else:
        return False


class User(BaseModel):
    name: str
    age: conint(ge=0, le=100)

    @computed_field
    def adult(self) -> bool:
        return val_adult(self.age)

    message: str = None


class Mapping(BaseModel):
    list_of_ids: list[typing.Any]
    tags: list[typing.Any]


def val_date(value: str) -> str:
    try:
        datetime.datetime.strptime(value, "%d/%m/%Y")
    except ValueError as e:
        raise e
    return value


last_date = Annotated[str, AfterValidator(val_date)]


class Meta(BaseModel):
    last_modification: last_date
    list_of_skills: list[str] = None
    mapping: Mapping


class BigJson(BaseModel):
    """Использует модель User."""
    user: User
    meta: Meta

# class UserRequest(BaseModel):
#     name: str
#     message: str
#
#
# class User(BaseModel):
#     name: str
#     age: str
#     is_adult: bool
#     message: str = None
#
#
# class UserResponse(BaseModel):
#     pass
