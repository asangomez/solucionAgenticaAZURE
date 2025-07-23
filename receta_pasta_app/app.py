import os
import requests
import chatlit
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
AZURE_FUNCTION_URL = os.getenv("AZURE_FUNCTION_URL")

def obtener_receta(tipo_pasta):
    response = requests.post(AZURE_FUNCTION_URL, json={"tipo": tipo_pasta})
    if response.status_code == 200:
        return response.json().get("receta")
    return "No se pudo obtener la receta en este momento."

if __name__ == "__main__":
    chat = chatlit.Chat()
    print("¡Bienvenido al recomendador de recetas de pasta! Pregúntame qué pasta cocinar.")
    while True:
        user_input = input("Tú: ")
        if "receta" in user_input.lower():
            tipo_pasta = None
            for pasta in ["espaguetis", "penne", "fettuccine"]:
                if pasta in user_input.lower():
                    tipo_pasta = pasta
                    break
            if tipo_pasta:
                receta = obtener_receta(tipo_pasta)
                print(f"Receta para {tipo_pasta}: {receta}")
            else:
                print("¿Qué tipo de pasta te gustaría preparar?")
        else:
            response = chat.chat(user_input)
            print("Asistente:", response)
