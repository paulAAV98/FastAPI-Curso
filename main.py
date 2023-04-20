from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Creacion de una aplicacion FastAPI:
app = FastAPI()

aplicacion = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get('/')
def read_mundo():
    return {'Hello': 'World!'}

@app.get('/hola')
def hola_mundo():
    return {'Hola' : 'Mundo'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
# = None significa opcional
    return {'item_id': item_id, 'q': q}


@app.get('/calculadora/{numero_1}{numero_2}')
def calculadora(numero_1: int, numero_2: int):
    return {'resultado': numero_1 + numero_2}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}