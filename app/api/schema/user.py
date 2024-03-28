from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    nickname: str
    email: EmailStr
    password: str


class GetUser(BaseModel):
    id: int
    nickname: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True


class UpdateUser(BaseModel):
    nickname: str
