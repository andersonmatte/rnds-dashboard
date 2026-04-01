import json
import plotly.express as px


def criar_mapa_brasil(df):

    # Carrega o mapa do Brasil
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

        color="vl_indicador_calculado_uf",

        hover_name="no_uf",

        hover_data={
            "sg_uf": True,
            "vl_indicador_calculado_uf": ":,.0f"
        },

        color_continuous_scale="Blues",

        title="Total de registros enviados para a RNDS por UF"
    )

    fig.update_geos(

        fitbounds="locations",

        visible=False

    )

    fig.update_layout(

        margin=dict(
            l=0,
            r=0,
            t=50,
            b=0
        )

    )

    return fig