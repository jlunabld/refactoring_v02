import dash_bootstrap_components as dbc
from dash import html

def usage_comparison():
    return dbc.Tab(
        label="YTD Bldng Usage Comparison Chart",
        className="border-primary text-dark",
        style={
            "backgroundColor": "transparent",
            "opacity": 1,
            "padding": "1px",
        },
        active_label_class_name="selected-tab",
        children=html.Div(
            id="YTD",
            style={"overflow": "scroll", "resize": "both"},
        )
    )