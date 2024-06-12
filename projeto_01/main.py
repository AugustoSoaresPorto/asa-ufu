from fastapi import FastAPI
from typing import Optional
from models.database import engine
from routers.alunos import router as router_alunos
from models.alunos import Alunos
from models.alunos import Base
from routers.cursos import router as router_cursos
from models.cursos import Cursos
from models.cursos import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_alunos)
app.include_router(router_cursos)
