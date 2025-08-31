from fastapi import APIRouter, HTTPException
from app.models import Atleta
from app.database import atletas_collection

router = APIRouter()

@router.post("/atletas")
async def criar_atleta(atleta: Atleta):
    atleta_dict = atleta.dict()
    result = await atletas_collection.insert_one(atleta_dict)
    atleta_dict["_id"] = str(result.inserted_id)
    return atleta_dict

@router.get("/atletas")
async def listar_atletas():
    atletas = []
    async for atleta in atletas_collection.find():
        atleta["_id"] = str(atleta["_id"])
        atletas.append(atleta)
    return atletas

@router.get("/atletas/{nome}")
async def buscar_atleta(nome: str):
    atleta = await atletas_collection.find_one({"nome": nome})
    if not atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    atleta["_id"] = str(atleta["_id"])
    return atleta
