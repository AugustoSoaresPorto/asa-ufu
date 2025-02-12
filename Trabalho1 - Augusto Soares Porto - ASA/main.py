# Aluno: Augusto Soares Porto - 12121ECP016

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Aluno(BaseModel):
  nome: str
  matricula: str
  curso: str
    
base_alunos = []    

@app.get("/")
async def root():
  return {"mensagem" : "Maravilha!"}

# Função GET 
@app.get("/alunos")
async def root():
  return {"mensagem" : base_alunos}    

# Função POST
@app.post("/alunos")
async def alunos(aluno: Aluno):
  for i in range(len(base_alunos)):
    if base_alunos[i].matricula == aluno.matricula:
      print("MATRÍCULA JÁ EXISTE!")
      print(base_alunos)
      return aluno   
  print("ITEM ADICIONADO!")
  base_alunos.append(aluno)
  print(base_alunos)
  return aluno

# Função PUT
@app.put("/alunos")
async def alunos(aluno: Aluno):
  for i in range(len(base_alunos)):
    if base_alunos[i].matricula == aluno.matricula:
      base_alunos[i] = aluno
      print("ITEM ATUALIZADO!")
      print(base_alunos)
      return aluno
  print("ITEM NÃO ENCONTRADO!")
  print(base_alunos)
  return aluno
    

# Função DELETE
@app.delete("/alunos")
async def alunos(aluno: Aluno):
  for i in range(len(base_alunos)):
    if base_alunos[i].matricula == aluno.matricula:
      del(base_alunos[i])
      print("ITEM DELETADO!")
      print(base_alunos)
      return aluno
  print("ITEM NÃO ENCONTRADO!")
  print(base_alunos)
  return aluno

'''
------------------ CASOS DE TESTE ------------------

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"nome":"Joao","matricula":"1", "curso":"ENG COMP"}' \
  http://localhost:8000/alunos

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"nome":"Pedro","matricula":"2", "curso":"ENG COMP"}' \
  http://localhost:8000/alunos

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"nome":"Arthur","matricula":"3", "curso":"ENG COMP"}' \
  http://localhost:8000/alunos

curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"nome":"Giovana","matricula":"2", "curso":"ENG AUTO"}' \
  http://localhost:8000/alunos

curl --header "Content-Type: application/json" \
  --request DELETE \
  --data '{"nome":"","matricula":"1", "curso":""}' \
  http://localhost:8000/alunos
'''