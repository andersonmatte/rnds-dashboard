from dash import html, dcc
from components.grafico_mapa_brasil import criar_mapa_brasil


## Aba do Brasil
def layout_aba_brasil(df):
    fig = criar_mapa_brasil(df)

    total_brasil = int(
        df["vl_indicador_calculado_br"].max()
    )

    total_formatado = (
        f"{total_brasil:,.0f}"
        .replace(",", ".")
    )

    return html.Div([
        html.Div(

            [

                html.H4(
                    "Total de registros no Brasil"
                ),

                html.H1(
                    total_formatado
                )

            ],

            style={
                "backgroundColor": "#f2f2f2",
                "padding": "15px",
                "borderRadius": "8px",
                "marginBottom": "20px",
                "textAlign": "center"
            }

        ),

        dcc.Graph(
            figure=fig,
            style={
                "height": "75vh"
            }
        )

    ])
