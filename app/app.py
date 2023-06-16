# Libraries
from dash import Dash, html
import dash_bootstrap_components as dbc
# Modules
from tabs.saving_opportunities import savings_opportunities
from tabs.usage_comparison import usage_comparison


class RMSDashboard:
    """ This class creates the RMS Dashboard. """
    def __init__(self):
        self.app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.set_layout()
        self.server = self.app.server

    def set_layout(self):
        self.app.layout = dbc.Container(
            [
                self.create_div()
            ]
        )

    def create_div(self):
        return html.Div(
            [
                dbc.CardHeader(
                    self.create()
                )
            ],
            className='my-custom-class'
        )

    def create(self):
        return dbc.Tabs(
            [
                savings_opportunities(),
                usage_comparison()
            ]
        )

    def run(self, debug=False):
        self.app.run_server(debug=debug)

server = RMSDashboard().server

if __name__ == '__main__':
    my_app = RMSDashboard()
    my_app.run(debug=True)