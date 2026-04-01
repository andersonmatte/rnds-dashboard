import json
import pandas as pd

## Função para formatar o ano-mes
def formatar_anomes(valor):
    valor = str(valor)

    ano = valor[:4]
    mes = valor[4:]

    return f"{mes}/{ano}"

## Carrega os dados
def carregar_dados():

    with open("data/rnds.json", encoding="utf-8") as f:
        dados = json.load(f)

    df = pd.DataFrame(dados)

    # Converter co_anomes -> MM/YYYY
    df["co_anomes_formatado"] = df["co_anomes"].apply(
        formatar_anomes
    )

    # Garantir numérico
    df["vl_indicador_calculado_uf"] = pd.to_numeric(
        df["vl_indicador_calculado_uf"]
    )

    df["vl_indicador_calculado_reg"] = pd.to_numeric(
        df["vl_indicador_calculado_reg"]
    )

    df["vl_indicador_calculado_br"] = pd.to_numeric(
        df["vl_indicador_calculado_br"]
    )

    # Converter data
    df["dt_atualizacao"] = pd.to_datetime(
        df["dt_atualizacao"]
    )

    return df