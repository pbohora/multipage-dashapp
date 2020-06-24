from dash.dependencies import Input,Output
from datetime import datetime as dt
import re

from app import app
from layouts import df
import pandas as pd

def filter_data(start_date, end_date, value, direction=None):
     if start_date and end_date is not None:
        start_date= dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
        start_date_string = start_date.strftime('%d/%m/%Y')
        end_date= dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
        end_date_string = end_date.strftime('%d/%m/%Y')        
        df_selected = df.loc[(df["Current_Match"] > start_date_string) & (df["Current_Match"] <= end_date_string)]
        if direction is not None:
            df_selected = df_selected[df_selected.Direction == direction]
        if value is not None:
            df_selected = df_selected[df_selected.Country == value]

        return df_selected


#datepicker callback
@app.callback(
    Output("output-container-date-picker-range-imports", "children"),
    [Input("date-picker-range-imports", "start_date"),
     Input("date-picker-range-imports", "end_date")])
def update_output(start_date, end_date):
    string_to_return = "You have selected "
    
    if start_date is not None:
        start_date= dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
        start_date_string = start_date.strftime('%m/%d/%Y')
        string_to_return = string_to_return + "the date range of " + start_date_string+ ' - '
        
    if end_date is not None:
        end_date= dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
        end_date_string = end_date.strftime('%m/%d/%Y')
        string_to_return = string_to_return + end_date_string
    
    return string_to_return

#imports callback
@app.callback(
    Output("datatable-imports", "data"),
    [Input("date-picker-range-imports", "start_date"),
     Input("date-picker-range-imports", "end_date"),
     Input("dropdown-imports", "value")])
def update_table(start_date, end_date, value):
    direction = "Imports"
    df_filtered =filter_data(start_date, end_date, value, direction)
    return df_filtered.to_dict('rows')

#exports callback      
@app.callback(
    Output("datatable-exports", "data"),
    [Input("date-picker-range-imports", "start_date"),
     Input("date-picker-range-imports", "end_date"),
     Input("dropdown-imports", "value")])
def update_table(start_date, end_date, value):
    direction = "Exports"
    df_filtered =filter_data(start_date, end_date, value, direction)
    return df_filtered.to_dict('rows')

#graph callback

@app.callback(
    Output("graph-imports-exports", "figure"),
    [Input("date-picker-range-imports", "start_date"),
     Input("date-picker-range-imports", "end_date"),
     Input("dropdown-imports", "value")])
def update_graph(start_date, end_date, value):
    direction_import = "Imports"
    direction_export = "Exports"
    df_filtered_import = filter_data(start_date, end_date, value, direction_import)
    df_filtered_export = filter_data(start_date, end_date, value, direction_export)
    
    traces = [dict(
            x=df_filtered_import[df_filtered_import['Country']==i]["Value"],
            y=df_filtered_export[df_filtered_export['Country']==i]["Value"],
            type= 'linear',
            mode='markers',
            text=df_filtered_import[df_filtered_import['Country']==i]["Current_Match"],
            marker={
                'size':12,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
            ) for i in df["Country"].unique()]
   
    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 'Import'},
            yaxis={'title': 'Export'},
            hovermode='closest',
           
        )
    }
    

