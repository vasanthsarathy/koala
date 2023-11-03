import os
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import json
import random
from koala.agent import graphit
import codecs

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.YETI, dbc.icons.FONT_AWESOME])
server = app.server #nee

LINE_BREAK = dbc.Row(html.Br())
LINE = dbc.Row(html.Hr())

# Top heading and logo
heading = [html.H2("🐨 KOALA"),html.H5("Knowledge-Oriented Abstract Language Analyzer")]
HEADER_ROW = dbc.Row(dbc.Col(heading, width={'size':5, 'offset':1}, align="center"))

# Input row 
utterance_group = dbc.InputGroup(
    [
        dbc.InputGroupText("Utterance: "),
        dbc.Input(id="utterance-input", placeholder="type your utterance here"),
    ]
)
INPUT_ROW = dbc.Row(dbc.Col(utterance_group, width={'size':5, 'offset':1}, align="center"))

# Output Row 
OUTPUT_ROW = dbc.Row(dbc.Col(id="graph-output", width={'size':11, 'offset':1}, align="center"))

# DASH APP LAYOUT
app.layout = html.Div([LINE_BREAK,
                       HEADER_ROW,
                       LINE_BREAK,
                       LINE,
                       INPUT_ROW,
                       LINE_BREAK,
                       OUTPUT_ROW
                       ])


############# CALLBACKS ############################
@app.callback(
    Output("graph-output", "children"),
    [Input("utterance-input", "value")],
)
def on_button_click(utterance):
    print(utterance)
    return utterance+", meow!"
    #graphit()
    #graph_loc = "graph.html"
    #print("graph made")
    #graph = open("graph.html", "r").read()
    #return html.Iframe(srcDoc=graph,style={"height": "1067px", "width": "80%"})



#########################

def main():
    server.run(debug=True, port=8010)

if __name__ == "__main__":
    app.run_server(debug=True)
