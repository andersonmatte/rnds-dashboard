import json
import pandas as pd
from dash import Dash, html, dcc
from services.data_loader import carregar_dados
import plotly.express as px

# Carrega os dados
dados = carregar_dados()

# Converter para DataFrame
df = pd.DataFrame(dados)

# Criar gráfico bar
figBar = px.bar(
    df,
    x="sg_uf",
    y="vl_indicador_calculado_uf",
    title="Total de registros enviados para a RNDS por UF"
)

# Criar gráfico pie
figPie = px.pie(
    df,
    names="sg_uf",
    values="vl_indicador_calculado_uf",
    title="Total de registros enviados para a RNDS por UF"
)


# Criar aplicação Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard RNDS"),

    dcc.Graph(
        figure=figBar,
    ),
    dcc.Graph(
        figure=figPie,
    )
])

if __name__ == "__main__":
    app.run(debug=True)