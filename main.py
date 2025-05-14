from fastapi import FastAPI
import json
import random
from pydantic import BaseModel
from typing import List, Optional
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar la carpeta para servir imágenes estáticas (si las usas localmente)
app.mount("/static", StaticFiles(directory="images"), name="static")

# Cargar preguntas desde el archivo JSON
with open("dataP1.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    questionsP1 = data["questions"]

# Cargar preguntas desde el archivo JSON
with open("dataP2.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    questionsP2Final = data["questions"]
    
# Cargar preguntas desde el archivo JSON
with open("dataP3.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    questionsP3Final = data["questions"]

# Modelo de respuesta para una pregunta
class QuestionResponse(BaseModel):
    code: int
    msg: str
    data: dict
    request_id: str

# Generar un ID aleatorio (simulación de request_id)
def generate_request_id():
    return str(random.randint(1000000000, 9999999999))

# Endpoint para obtener una pregunta aleatoria de la parte 1
@app.get("/api/randomquestionP1", response_model=QuestionResponse)
def get_random_questionP1():
    question = random.choice(questionsP1)

    response = {
        "code": 200,
        "msg": "Pregunta obtenida con éxito",
        "data": {
            "context": question["context"],
            "question": question["question"],
            "options": question["options"],
            "correct_answer": question["correct_answer"],
            "image": question["image"]
        },
        "request_id": generate_request_id()
    }

    return response

# Endpoint para obtener una pregunta aleatoria de la parte 2
@app.get("/api/randomquestionP2", response_model=QuestionResponse)
def get_random_questionP2():
    question = random.choice(questionsP2Final)

    response = {
        "code": 200,
        "msg": "Pregunta obtenida con éxito",
        "data": {
            "context": question["context"],
            "question": question["question"],
            "options": question["options"],
            "correct_answer": question["correct_answer"],
            "image": question["image"]
        },
        "request_id": generate_request_id()
    }

    return response

# Endpoint para obtener una pregunta aleatoria de la parte 3
@app.get("/api/randomquestionP3", response_model=QuestionResponse)
def get_random_questionP3():
    question = random.choice(questionsP3Final)

    response = {
        "code": 200,
        "msg": "Pregunta obtenida con éxito",
        "data": {
            "context": question["context"],
            "question": question["question"],
            "options": question["options"],
            "correct_answer": question["correct_answer"],
            "image": question["image"]
        },
        "request_id": generate_request_id()
    }

    return response
