import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_bootstrap_templates import load_figure_template
from src import utils

load_figure_template('Darkly')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.B('Codigo Modelo'),
                dcc.Dropdown(
                    options={},
                    placeholder="Pesquisar pelo codigo do Modelo ou Nome do Modelo",
                    optionHeight=50,
                    maxHeight=50,
                    multi=False,
                    id='dropdown_cod_modelo'
                )
            ],
            style=dict(
                width='20%',
                #display='inline-block',
                marginTop='10px',
                marginRight='10px',
                marginBottom='10px',
                marginLeft='10px'
            ),
        ),

        html.Div(
            children=[
                html.B('Filtros'),
                html.Div('Modelo'),
                dcc.Dropdown(
                    options=['COMPRADO', 'VENDIDO'],
                    placeholder="Selecione Modelo",
                    optionHeight=50,
                    multi=True
                ),
                html.Br(),
                html.Div('Pessoa'),
                dcc.Dropdown(
                    options=['PF', 'PJ'],
                    placeholder="Selecione Pessoa",
                    multi=True,
                    optionHeight=50,
                ),
            ],
            style=dict(
                width='20%',
                #display='inline-block',
                marginTop='10px',
                marginRight='10px',
                marginBottom='10px',
                marginLeft='10px'
            ),
        ),
        html.Div(
            children=[
                html.Br(),
                html.Div('Performance'),
                dcc.Dropdown(
                    options=['KS Alto', 'KS Baixo'],
                    placeholder="Selecione Performance",
                    optionHeight=50,
                    multi=True

                ),
                html.Br(),
                html.Div('Conversão'),
                dcc.Dropdown(
                    options=["Alta", "Baixa"],
                    placeholder="Selecione Conversão",
                    optionHeight=50,
                    multi=True
                ),
            ],
            style=dict(
                width='20%',
                #display='inline-block',
                marginTop='10px',
                marginRight='10px',
                marginBottom='10px',
                marginLeft='10px'
            ),
        ),

        html.Div(
            children=[
                html.Br(),
                html.Div("Data Avaliação"),
                dcc.Dropdown(
                    options=utils.get_target_dates(),
                    placeholder="Selecione Data Avaliação",
                    optionHeight=50,
                    maxHeight=700,
                    multi=True
                ),
                html.Br(),
                html.Div("Data Escoragem"),
                dcc.Dropdown(
                    options=utils.get_scoring_dates(),
                    placeholder="Selecione Data Escoragem",
                    optionHeight=50,
                    maxHeight=700,
                    multi=True
                ),
            ], style=dict(
                width='20%',
                #display='inline-block',
                marginTop='10px',
                marginRight='10px',
                marginBottom='10px',
                marginLeft='10px'),
        ),
    ]
)
app.run_server(debug=True)
