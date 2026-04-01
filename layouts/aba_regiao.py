from dash import html, dcc

from components.grafico_regiao import criar_grafico_regiao

def layout_aba_regiao(df):

    fig = criar_grafico_regiao(df)

    return html.Div([

        dcc.Graph(
            figure=fig
        )

    ])