def main(req):
    tipo = req.get_json().get("tipo", "").lower()
    recetas = {
        "espaguetis": "Receta de espaguetis carbonara: pasta, huevo, queso, panceta, pimienta.",
        "penne": "Receta de penne arrabbiata: pasta, tomate, ajo, chili, aceite de oliva.",
        "fettuccine": "Receta de fettuccine Alfredo: pasta, mantequilla, queso parmesano."
    }
    receta = recetas.get(tipo, "Lo siento, no tengo una receta para ese tipo de pasta.")
    return {"receta": receta}
