from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    """
    API-ToDo - Metodo Get - retorna uma mensagem
    """
    return {'message': 'Ola, funcionou. Estamos respondendo da raiz da API!!!'}
