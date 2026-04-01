from dash import Dash, html, dcc

from services.data_loader import carregar_dados

from layouts.aba_uf import layout_aba_uf
from layouts.aba_regiao import layout_aba_regiao
from layouts.aba_brasil import layout_aba_brasil

# Carrega dados uma vez
df = carregar_dados()

app = Dash(__name__)

app.layout = html.Div([

    html.H1("Dashboard RNDS"),

    dcc.Tabs([

        dcc.Tab(
            label="Por UF",
            children=layout_aba_uf(df)
        ),

        dcc.Tab(
            label="Por Região",
            children=layout_aba_regiao(df)
        ),

        dcc.Tab(
            label="Brasil",
            children=layout_aba_brasil(df)
        )

    ])

])

if __name__ == "__main__":
    app.run(debug=True)