import plotly.express as px

def criar_grafico_regiao(df):

    df_regiao = (
        df
        .groupby("no_regiao_brasil")
        ["vl_indicador_calculado_uf"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        df_regiao,
        x="no_regiao_brasil",
        y="vl_indicador_calculado_uf",
        title="Total de registros enviados para a RNDS por Região"
    )

    return fig