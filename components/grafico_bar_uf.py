import plotly.express as px


## Cria o gráfico de barra
def criar_grafico_bar_uf(df):
    fig = px.bar(
        df,
        x="sg_uf",
        y="vl_indicador_calculado_uf",
        title="Total de registros enviados para a RNDS por UF",
        labels={
            "sg_uf": "UF",
            "vl_indicador_calculado_uf": "Total de Registros"
        },
    )

    return fig
