from dash.dependencies import Input,Output
from datetime import datetime as dt

from app import app
from layouts import df

@app.callback(
    Output("output-container-date-picker-range-imports", "children"),
    [Input("date-picker-range-imports", "start_date"),
     Input("date-picker-range-imports", "end_date")])
def update_output(start_date, end_date):
    string_to_return = "You have selected "
    print(type(start_date),end_date)
    if start_date is not None:
        string_to_return = string_to_return + "the date range of " + start_date+ ' - '
        
    if end_date is not None:
        string_to_return = string_to_return + end_date
    
    return string_to_return

@app.callback(
    Output("datatable-imports", "data"),
    [Input("date-picker-range-imports", "start_date"),
     Input("date-picker-range-imports", "end_date"),
     Input("dropdown-imports", "value")])
def update_table(start_date, end_date, value):
    if start_date and end_date is not None:
        print(type(end_date.to_pydatetime()))
        df_imports = df[df.Direction == "Imports"]
        df_selected = df_imports[(df_imports.Current_Match > start_date) & (df_imports.Current_Match <= end_date)]
        if value is not None:
            df_selected = df_selected[df_selected.Country == value]
        print(df_selected)
        return df_selected.to_dict('rows')
       
        
       

