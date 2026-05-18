from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RecordCreate(BaseModel):
    title: str
    content: str


class JobCreate(BaseModel):
    target_url: str
