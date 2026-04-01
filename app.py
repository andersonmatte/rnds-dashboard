from dash import Dash, html, dcc

from services.data_loader import carregar_dados

from components.grafico_bar_uf import criar_grafico_bar_uf
from components.grafico_pie_uf import criar_grafico_pie_uf

# Carrega dados
df = carregar_dados()

# Cria gráficos
figBar = criar_grafico_bar_uf(df)
figPie = criar_grafico_pie_uf(df)

# App
app = Dash(__name__)

app.layout = html.Div([

    html.H1("Dashboard RNDS"),

    dcc.Graph(
        figure=figBar
    ),

    dcc.Graph(
        figure=figPie
    )

])

if __name__ == "__main__":
    app.run(debug=True)