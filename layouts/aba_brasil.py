from dash import html, dcc

from components.grafico_mapa_brasil import criar_mapa_brasil

def layout_aba_brasil(df):

    fig = criar_mapa_brasil(df)

    return html.Div([

        html.H2(
            "Distribuição de registros enviados para a RNDS por UF"
        ),

        dcc.Graph(
            figure=fig
        )

    ])