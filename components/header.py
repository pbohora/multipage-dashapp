import dash_core_components as dcc
import dash_html_components as html
import dash_table

from datetime import datetime as dt 
import pandas as pd 

def Header():
    df = pd.read_csv("data/datafile.csv")
    df = df.sort_values(by='Current_Match')
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
            html.Div([
            dcc.DatePickerRange(
                id="date-picker-range-imports",
                min_date_allowed = dt.strptime(date.min(),"%d/%m/%Y"),
                max_date_allowed = dt.strptime(date.max(),"%d/%m/%Y"),
                initial_visible_month =dt.strptime(date.min(),"%d/%m/%Y"),
                start_date = dt(2020, 5, 1),
                end_date =  dt(2020, 5, 30)
            ),
            html.Div(id="output-container-date-picker-range-imports")
            
        ], className = "date-picker",),
         html.Div([
            html.Label("Select by country"),
            dcc.Dropdown(
                options=[{"label":i,"value":i} for i in countries], 
                id = "dropdown-imports"
            ),
        ], className = "dropdown"),
    ], className = "filter-section")

    ],
    className="app-header")

    return header



