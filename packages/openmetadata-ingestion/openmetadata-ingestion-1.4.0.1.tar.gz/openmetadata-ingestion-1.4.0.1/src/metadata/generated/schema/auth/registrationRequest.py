# generated by datamodel-codegen:
#   filename:  auth/registrationRequest.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field, constr

from ..type import basic


class RegistrationRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    firstName: str = Field(..., description='First Name')
    lastName: str = Field(..., description='Last Name')
    email: basic.Email = Field(..., description='Email address of the user.')
    password: constr(min_length=8, max_length=56) = Field(
        ..., description='Login Password'
    )
