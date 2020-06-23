from dash.dependencies import Input,Output
from datetime import datetime as dt 

from app import app

@app.callback(
    Output("output-container-date-picker-range-imports", "children"),
    [Input("date-picker-range-imports", "start_date"),
     Input("date-picker-range-imports", "end_date")])
def update_output(start_date, end_date):
    string_to_return = "You have selected "
    print(start_date, end_date)
    if start_date is not None:
        string_to_return = string_to_return + "the date range of " + start_date+ ' - '
        
    if end_date is not None:
        string_to_return = string_to_return + end_date
    
    return string_to_return

# @app.callback(
#     Output("datatable-imports", "data"),
#     [Input("date-picker-range-imports", "start_date"),
#      Input("date-picker-range-imports", "end_date")])
# def update_table(start_date, end_date):
#     if start_date is not None:
       
        
       
#     if end_date is not None:
       
        
       

