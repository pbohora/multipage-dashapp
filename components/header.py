import dash_core_components as dcc
import dash_html_components as html
import dash_table

from datetime import datetime as dt 
import pandas as pd 

def Header():
    df = pd.read_csv("data/datafile.csv")
    date =  df["Current_Match"]
    countries = df["Country"].unique()
   
    header = html.Div([
        html.H1(["Multi-page dash app"], className= "app-header--title"),
        html.Div([
            dcc.Link('Home', href='/'),
            dcc.Link('Imports', href='/imports'),
            dcc.Link('Exports', href='/exports')
            ], className = "nav-links"),
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

    ],
    className="app-header")

    return header



