import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Create Dash application
app = dash.Dash(__name__)

# Define layout of the application
app.layout = html.Div([
    # Dashboard title
    html.H1("Automobile Sales Statistics Dashboard", 
            style={
                'textAlign': 'center',     # Center align the text
                'color': '#503D36',        # Set text color
                'font-size': '24px'        # Set font size
            }),
    # Add more components here for dropdowns, graphs, etc.
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
