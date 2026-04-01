import plotly.express as px

def criar_grafico_tempo(df):

    df_tempo = (
        df
        .groupby("co_anomes_formatado")
        ["vl_indicador_calculado_br"]
        .max()
        .reset_index()
    )

    fig = px.line(
        df_tempo,
        x="co_anomes_formatado",
        y="vl_indicador_calculado_br",
        title="Evolução dos registros enviados para a RNDS"
    )

    return fig