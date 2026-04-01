from dash import html, dcc

from components.grafico_bar_uf import criar_grafico_bar_uf
from components.grafico_pie_uf import criar_grafico_pie_uf

def layout_aba_uf(df):

    figBar = criar_grafico_bar_uf(df)
    figPie = criar_grafico_pie_uf(df)

    return html.Div([

        dcc.Graph(
            figure=figBar
        ),

        dcc.Graph(
            figure=figPie
        )

    ])