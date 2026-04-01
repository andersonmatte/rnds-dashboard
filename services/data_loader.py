import json
import pandas as pd

def carregar_dados():
    with open("data/rnds.json", encoding="utf-8") as f:
        dados = json.load(f)

    return pd.DataFrame(dados)