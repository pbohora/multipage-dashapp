import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
import callbacks
from layouts import layout_imports, layout_exports


app.index_string = ''' 
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Multipage dash app</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

app.layout= html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content")
    ])

@app.callback(Output("page-content", "children"),
              [Input("url","pathname")])
def display_page(pathname):
    if pathname=="/":
        return "hello home"
    elif pathname=="/imports":
        return layout_imports
    elif pathname=="/exports":
        return layout_exports
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)