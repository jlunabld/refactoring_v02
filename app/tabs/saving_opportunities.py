import dash_bootstrap_components as dbc
from dash import html

def savings_opportunities():
    """This function returns the Savings Opportunities tab."""
    return dbc.Tab(
        label="Savings Opportunities",
        className="border-primary text-dark",
        style={
            "backgroundColor": "transparent",
            "opacity": 1,
            "padding": "1px",
        },
        active_label_class_name="selected-tab",
        children=html.Div(
            id="Savings",            
            style={"overflow": "scroll", "resize": "both"},
        )
    )