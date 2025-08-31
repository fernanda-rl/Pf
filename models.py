from pydantic import BaseModel

class Atleta(BaseModel):
    nome: str
    idade: int
    peso: float
    categoria: str
