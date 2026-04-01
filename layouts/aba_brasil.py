from dash import html, dcc

from components.grafico_mapa_brasil import criar_mapa_brasil


## Aba do Brasil
def layout_aba_brasil(df):
    fig = criar_mapa_brasil(df)

    return html.Div([
        dcc.Graph(
            figure=fig,
            style={
                "height": "650px"
            }
        )

    ])
