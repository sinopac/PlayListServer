from typing import Optional
from pydantic import BaseModel, EmailStr, validator


class UserSchema(BaseModel):
    last_name: str
    middle_name: Optional[str]
    first_name: str
    email: EmailStr
    password: str
    password1: str

    @validator("password1")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("passwords do not match")
        return v
