# Challenge_Kosmos_Paulo_Villa
En este repositorio se encontrará la solución para el Challenge de Kosmos para la posición de Machine Learning Engineer


Una vez descargado el Repositorio. Debes seguir estos pasos:

### 1) Crear un virtual environment

### 2) Activar el virtual environment

### 3) Instalar los requerimientos de la aplicación.

``pip install -r requirements.txt``

### 4) Instalar el modelo de lenguaje en español de spacy

``python -m spacy download es_core_news_sm``

### 5) Correr la aplicación

``python main.py``


Ahora podrás hacer distintas consultas de esta API en aplicaciones como Postman:

* En el puerto http://0.0.0.0:8000/ (get) será un endpoint home para ver si funciona nuestra api

* En el puerto http://0.0.0.0:8000/ner?password=ml_engineer podrás ver las entidades de 
las oraciones que mandes con el formato body como un JSON. (No olvides la contraseña)
  * ej -> ``{
   "oraciones": ["Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
   "San Francisco considera prohibir los robots de entrega en la acera."]
}``