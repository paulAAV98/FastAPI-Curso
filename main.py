from typing import Union
from fastapi import FastAPI

# Creacion de una aplicacion FastAPI:
app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World!'}

app.get('/hola')
def hola_mundo():
    return {'Hola' : 'Mundo'}