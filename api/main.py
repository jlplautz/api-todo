import mongoengine
from fastapi import FastAPI

mongoengine.connect('todo_api_db', host='mongodb://localhost')  # to create a default connection

app = FastAPI()


@app.get('/')
def home():
    """
    API-ToDo - Metodo Get - retorna uma mensagem
    """
    return {'message': 'Ola, funcionou. Estamos respondendo da raiz da API!!!'}
