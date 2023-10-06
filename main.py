from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKey
from starlette.status import HTTP_403_FORBIDDEN
from pydantic import BaseModel
from typing import List
import uvicorn
import spacy

# Definimos una contraseña para el usuario que haga consultas a la API
API_KEY = "ml_engineer"
API_KEY_NAME = "password"

# Definimos el parámetro de la consulta.
api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)

# Creamos nuestra API
app = FastAPI(
    # Definimos título, descripción y versión
    title="MLE Challenge",
    description="Esta API recibe un parámetro tipo body con una petición POST que contenga un JSON con una lista de "
                "oraciones en español. La API debe devolver un JSON  una lista de las entidades identificadas en"
                "cada oración, junto con el tipo de cada entidad.",
    version="0.0.1"
)


# Definimos el tipo de entrada de los datos.
class DatosEntrada(BaseModel):
    oraciones: List[str]


# Definimos una función para que haga la validación de la contraseña.
def get_api_key(api_key_query: str = Security(api_key_query)):
    # En caso de que la contraseña sea correcta creamos la variable de la consulta.
    if api_key_query == API_KEY:
        return api_key_query
    # Si la contraseña es incorrecta, se levanta un error.
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Acceso denegado."
        )


# Descargamos el tokenizador en español, con la función NER.
nlp = ...#spacy.load("es_core_news_sm")


# Definimos un endpoint de home, únicamente para revisar el funcionamiento de la api
@app.get("/")
def home():
    return {"Descripción": "Health Check"}


# Creamos la función ner que recibirá una lista con oraciones.
def recon_entities(oraciones_list: list):
    # Definimos una lista donde se van a almacenar los resultados.
    res = []
    # Ciclo para recorrer las oraciones.
    for oracion in oraciones_list:
        # Utilizamos la función NER
        doc = nlp(text=oracion)
        # Creamos el diccionario donde se desglosarán las entidades
        entities = {}
        # Empezamos el ciclo por entidad
        for ent in doc.ents:
            # Agregamos al diccionario de la forma -> {oración: entidad}
            entities[ent.text] = ent.label_
        # Agregamos los resultados a la lista definida arriba.
        res.append({
            "Oración": oracion,
            "Entidades": entities
        })
    return res


# Definimos nuestra función NER
@app.post("/ner")
def print_entities(data: DatosEntrada,  api_key: APIKey = Depends(get_api_key)):
    oraciones = data.oraciones
    resultados = recon_entities(oraciones)
    return {"Resultado": resultados}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
