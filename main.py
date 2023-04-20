from typing import Union
from fastapi import FastAPI

# Creacion de una aplicacion FastAPI:
app = FastAPI()

aplicacion = FastAPI()

@app.get('/')
def read_mundo():
    return {'Hello': 'World!'}

@app.get('/hola')
def hola_mundo():
    return {'Hola' : 'Mundo'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}


@app.get('/calculadora/{numero_1}{numero_2}')
def calculadora(numero_1: int, numero_2: int):
    return {'resultado': numero_1 + numero_2}