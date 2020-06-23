import dash_core_components as dcc
import dash_html_components as html
import dash_table

# from components import Header, print_button
from datetime import datetime as dt 
# from datetime import date, timedelta
import pandas as pd 

df = pd.read_csv("data/datafile.csv")
date =  df["Current_Match"]
print(date)
countries = df["Country"].unique()

layout_imports = html.Div([
    html.Div([
        "I am header",
        
        html.Div([
            dcc.DatePickerRange(
                id="date-picker-range-imports",
                min_date_allowed = dt.strptime(date.min(),"%d/%m/%Y"),
                max_date_allowed = dt.strptime(date.max(),"%d/%m/%Y"),
                initial_visible_month =dt.strptime(date.min(),"%d/%m/%Y"),
                start_date = dt.strptime(date.min(),"%d/%m/%Y"),
                end_date = dt.strptime(date.max(),"%d/%m/%Y")
            ),
            html.Div(id="output-container-date-picker-range-imports")
            
        ]),

        html.Div([
            html.Label("Select by country"),
            dcc.Dropdown(
                options=[{"label":i,"value":i} for i in countries], 
                id = "dropdown-imports"
            ),
        ]),

        html.Div([
            dash_table.DataTable(
                id="datatable-imports",
                columns=[{"name":i, "id":i} for i in df.columns]
            )
        ]),

        html.Div([
            dcc.Graph(id="graph-imports")
        ])
    ])
])