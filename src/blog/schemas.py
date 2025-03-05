from pydantic import BaseModel, Field


class Utente(BaseModel):
    id: int = Field(..., examples=[1])
    name: str = Field(..., max_length=100, examples=["Nome dell'utente"])
    age: int = Field(..., max_length=3, examples=["Età dell'utente"])
