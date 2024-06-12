from fastapi          import APIRouter, Depends, HTTPException, Response, status
from models.cursos    import Cursos
from schemas.cursos   import CursosSchema
from sqlalchemy.orm   import Session
from models.database  import get_db
import logging
import coloredlogs, logging

router = APIRouter()

@router.get("/cursos")
def get(db: Session = Depends(get_db)):
    todos_cursos = db.query(Cursos).all()
    return todos_cursos

@router.post("/cursos")
def cria_cursos(curso: CursosSchema, db: Session = Depends(get_db)):
    novo_curso = Cursos(**curso.model_dump())
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)
    return novo_curso

@router.delete("/cursos/{id}")
def delete(id:int ,db: Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    delete_post = db.query(Cursos).filter(Cursos.id == id)
    
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Curso não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/cursos/{id}")
def update(id: int, curso:CursosSchema, db:Session = Depends(get_db)):
    updated_post = db.query(Cursos).filter(Cursos.id == id)
    updated_post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Curso: {id} does not exist')
    else:
        updated_post.update(curso.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()