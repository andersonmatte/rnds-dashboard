import plotly.express as px


## Cria o gráfico de pizza
def criar_grafico_pie_uf(df):
    fig = px.pie(
        df,
        names="sg_uf",
        values="vl_indicador_calculado_uf",
        title="Distribuição de registros enviados para a RNDS por UF",
        labels={
            "sg_uf": "UF",
            "vl_indicador_calculado_uf": "Total de Registros"
        },
    )

    return fig
