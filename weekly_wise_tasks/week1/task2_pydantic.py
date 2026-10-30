import re
from pydantic import BaseModel, Field, EmailStr, ValidationError, field_validator


class UserProfile(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, le=40)
    email: EmailStr
    pan: str

    @field_validator("pan")
    @classmethod
    def validate_pan(cls, value):
        pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"
        if not re.fullmatch(pattern, value):
            raise ValueError("Invalid PAN format. It should be in the format: AAAAA9999A")
        return value
# test data
data = {
    "name": "shivani",
    "age": 30,
    "email": "shivani@example.com",
    "pan": "ABCDE1234Z"
}
try:
    user = UserProfile(**data)
    print(user)
except ValidationError as e:
    print(e)

    