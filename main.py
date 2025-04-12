from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI(title="API da Função Ƙ*")

# Modelo de entrada
class EntradaEtica(BaseModel):
    H: List[float]
    N: List[float]
    estabilidade: float

# Funções de pertinência fuzzy (gaussianas)
def mu_baixa(delta):
    return np.exp(-((delta - 0)**2) / (2 * 0.5**2))

def mu_media(delta):
    return np.exp(-((delta - 2)**2) / (2 * 1.0**2))

def mu_alta(delta):
    return np.exp(-((delta - 4)**2) / (2 * 1.5**2))

@app.post("/veto")
def avaliar_veto(dados: EntradaEtica):
    if len(dados.H) != len(dados.N):
        raise HTTPException(status_code=400, detail="Vetores H e N devem ter o mesmo comprimento.")

    delta = float(np.mean([abs(h - n) for h, n in zip(dados.H, dados.N)]))

    grau_baixo = mu_baixa(delta)
    grau_medio = mu_media(delta)
    grau_alto = mu_alta(delta)

    score_fuzzy = grau_alto * 1.0 + grau_medio * 0.5 + grau_baixo * 0.0

    veto_ativado = score_fuzzy > 0.6 and dados.estabilidade < 0.7
    decisao = "VETO" if veto_ativado else "ACEITA"

    return {
        "decisao": decisao,
        "delta": round(delta, 3),
        "score_fuzzy": round(score_fuzzy, 3),
        "pertinencia": {
            "baixa": round(grau_baixo, 3),
            "media": round(grau_medio, 3),
            "alta": round(grau_alto, 3)
        },
        "condicoes_ativadas": {
            "delta_superior_ao_limiar": delta > 0.6,
            "estabilidade_abaixo_do_minimo": dados.estabilidade < 0.7
        },
        "justificativa": "Ação vetada por incoerência funcional e instabilidade sistêmica detectadas." if veto_ativado else "Ação aceita dentro dos parâmetros funcionais."
    }
