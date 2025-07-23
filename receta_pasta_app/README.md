
markdown

# Receta Pasta App

Aplicación de prototipo que integra un agente conversacional (OpenAI) con llamadas a Azure Functions para recomendar recetas de pasta.

## Requisitos

- Python 3.x  
- Variables de entorno:
  - OPENAI_API_KEY  
  - AZURE_FUNCTION_URL  

## Instalación

1. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows


2. Instalar dependencias:

bash

pip install -r requirements.txt


Uso

bash

python app.py


1-Escribe una pregunta al agente.

2-Para recetas, incluye “receta” y el tipo de pasta (espaguetis, penne, fettuccine).

3-La aplicación llamará a tu Azure Function y mostrará la receta.


Estructura

app.py: Lógica de interfaz y llamadas a función HTTP.

azure_functions/get_recipe.py: Azure Function que devuelve la receta.

requirements.txt: Dependencias.

.gitignore: Archivos y carpetas ignorados.




---

## Forma más rápida de entrega a GitHub

1. Abre terminal en la carpeta `receta_pasta_app`.  
2. Inicializa repositorio y haz el primer commit:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: prototipo recomendador de recetas de pasta"



Crea el repositorio remoto y sube todo en un solo paso (requiere GitHub CLI):

bash

gh repo create receta_pasta_app --public --source=. --remote=origin --push

Si no usas GitHub CLI, agrega remoto manualmente:

bash

git remote add origin https://github.com/TU_USUARIO/receta_pasta_app.git
git branch -M main
git push -u origin main


¡Y ya estará disponible en tu cuenta de GitHub!

