from pydantic import BaseModel, EmailStr, Field

class UserInput(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    role: str = Field(default="annotator")