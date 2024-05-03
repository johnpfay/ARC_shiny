from shiny import App, render, ui
import pandas as pd
from pathlib import Path

fn_LDAS = Path(__file__).parent / 'Peru_LDAS.csv'

#df_LDAS = pd.read_csv(
#    'Peru_LDAS.csv',
#    #"https://github.com/johnpfay/ARC_shiny/raw/main/data/processed/Peru_LDAS.csv",
#    dtype={'ubigeo':'str'},             #Read the ubigeo field as string
#    parse_dates=['EpiweekStartDate']    #Read the EpiweekStartDate as datetime
#).set_index(['ubigeo','EpiweekStartDate','year','week'])

app_ui = ui.page_fluid(
    ui.panel_title(f"Hello Shiny GO! {fn_LDAS.exists()} "),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)
