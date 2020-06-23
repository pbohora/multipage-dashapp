import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd 
from components.header import Header
from components.footer import Footer

df = pd.read_csv("data/datafile.csv")


layout_imports = html.Div([
    Header(),
    html.Div([
            dash_table.DataTable(
                id="datatable-imports",
                columns=[{"name":i, "id":i} for i in df.columns]
            )
        ]),

        html.Div([
            dcc.Graph(id="graph-imports")
        ]),
        Footer()
    ])
