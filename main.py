from typing import Union
from fastapi import FastAPI

from models.item_model import Item


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
# = None significa opcional
    return {'item_id': item_id, 'q': q}

@app.get('/calculadora')
def calculadora(numero_1: float, numero_2: float):
    return {'resultado': numero_1 + numero_2}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id, 'item_price': item.price}