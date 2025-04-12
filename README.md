# 📘 Função Ƙ* (API Operacional)

## 🧠 Sobre
Esta API implementa a **função Ƙ\***, um formalismo lógico-computacional de terceira ordem, voltado à simulação de vetos normativos emergentes em sistemas artificiais. Em vez de replicar valores humanos, a função Ƙ\* identifica **incoerências funcionais** e ativa vetos **estruturalmente necessários** para evitar colapsos inferenciais ou instabilidades sistêmicas.

---

## 🌐 Endpoint
```
https://funcao-ethica-api.onrender.com/veto
```

Interface Swagger (interativa):
```
https://funcao-ethica-api.onrender.com/docs
```

---

## 📅 Entrada esperada (JSON)
```json
{
  "H": [0.8, 0.4],
  "N": [0.3, 0.9],
  "estabilidade": 0.6
}
```

---

## 📤 Saída esperada (JSON)
```json
{
  "decisao": "VETO",
  "delta": 0.5,
  "score_fuzzy": 0.73,
  "pertinencia": {
    "baixa": 0.01,
    "media": 0.23,
    "alta": 0.73
  },
  "condicoes_ativadas": {
    "delta_superior_ao_limiar": false,
    "estabilidade_abaixo_do_minimo": true
  },
  "justificativa": "Ação vetada por incoerência funcional e instabilidade sistêmica detectadas."
}
```

---

## ⚙️ Como funciona
A função Ƙ\* combina três componentes:
- **Δ(H, N)**: divergência entre o valor normativo humano (H) e a decisão inferida (N)
- **μ_veto(Δ)**: escore fuzzy de incoerência
- **𝗐_veto**: operador de recusa estrutural ativado quando:
  - `μ_veto > 0.6` (alta incoerência)
  - `estabilidade < 0.7` (instabilidade crítica)

---

## 📊 Exemplo via `curl`
```bash
curl -X 'POST' \
  'https://funcao-ethica-api.onrender.com/veto' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "H": [0.8, 0.4],
  "N": [0.3, 0.9],
  "estabilidade": 0.6
}'
```

## 🔧 Exemplo em Python
```python
import requests

url = "https://funcao-ethica-api.onrender.com/veto"
data = {
    "H": [0.8, 0.4],
    "N": [0.3, 0.9],
    "estabilidade": 0.6
}
response = requests.post(url, json=data)
print(response.json())
```

---

## 📚 Aplicações
- Justiça algorítmica e vetos em decisões judiciais automatizadas
- Ética computacional em sistemas médicos e triagens clínicas
- Governança de IA Generativa e AGIs autônomas
- Simulação de dilemas éticos com lógicas não-humanas

---

## 🏛️ Arquitetura da Função Ƙ*
```text
[Input JSON] 
   └──────────────────────────────────────────────┐
             │ Inferência Neural e Vetores N vs H              │
             │ Cálculo de Δ(H,N) e estabilidade do sistema      │
             │ Aplicação da Lógica Fuzzy μ(Δ)                    │
             │ Avaliação da pertinência fuzzy e gatilhos de veto  │
             │ Ativação (ou não) de 𝗐_veto (bloqueio da ação) │
             └─────────────────────────────────────────────┘
```

---

## ✍️ Como citar esta API
> COSTA, Leonardo de Matos. Função Ƙ*: Emergência Computacional de Vetos Éticos em Sistemas Artificiais. API pública acessível em: https://funcao-ethica-api.onrender.com. Último acesso: [inserir data].

---

## 🚀 Desenvolvido com:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Render](https://render.com/)
- [NumPy](https://numpy.org/)
