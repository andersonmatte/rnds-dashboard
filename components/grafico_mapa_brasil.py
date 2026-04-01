import json

import plotly.express as px


## Componente do Mapa do Brasil
def criar_mapa_brasil(df):
    with open(
            "data/brasil_estados.geojson",
            encoding="utf-8"
    ) as f:
        geojson = json.load(f)

    fig = px.choropleth(
        df,
        geojson=geojson,
        locations="sg_uf",
        featureidkey="properties.sigla",
        color="no_regiao_brasil",
        hover_name="no_uf",
        hover_data={
            "no_regiao_brasil": True,
            "vl_indicador_calculado_uf": ":,.0f"
        },
        color_discrete_map={

            "Norte": "#1f77b4",
            "Nordeste": "#ff7f0e",
            "Centro-Oeste": "#2ca02c",
            "Sudeste": "#d62728",
            "Sul": "#9467bd"
        },
        title="Distribuição de registros enviados para a RNDS por Região",
        labels={
            "no_regiao_brasil": "Região",
            "sg_uf": "UF",
            "vl_indicador_calculado_uf": "Total de Registros"
        },
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    return fig
