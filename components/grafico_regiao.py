import plotly.express as px


## Componente do Gráfico de Região
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
        title="Total de registros enviados para a RNDS por Região",
        color="no_regiao_brasil",
        color_discrete_map={
            "Norte": "#1f77b4",
            "Nordeste": "#ff7f0e",
            "Centro-Oeste": "#2ca02c",
            "Sudeste": "#d62728",
            "Sul": "#9467bd"
        },
        labels={
            "no_regiao_brasil": "Região",
            "vl_indicador_calculado_uf": "Total de Registros"
        }
    )

    return fig
