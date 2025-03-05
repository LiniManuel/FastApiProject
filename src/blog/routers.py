from fastapi import APIRouter
from src.blog.schemas import Utente
from src.database import utenti

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)


@router.get("/list")
async def fetchUtenti():
    return utenti


@router.post("/post", response_model=list[Utente])
async def createUtente(content: Utente) -> list[Utente]:
    utenti.append(content)
    return utenti


@router.get("/get")
async def fetchUtente(id_post: int = 1):
    for utente in utenti:
        if utente["id"] == id_post:
            return utente["nome"]
