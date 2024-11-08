from flask import Flask, render_template, request
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from scripts.utility import Utility
from scripts.config import Config
import json

app = Flask(__name__)

def start_webui(utility: Utility) -> None:
    """Start the WebUI using Flask."""
    @app.route('/')
    def index():
        """Render the main index page."""
        return render_template('index.html')

    @app.route('/calculate_smma', methods=['POST'])
    def calculate_smma():
        """Calculate the SMMA and return a success message."""
        utility.calculate_smma()
        return "SMMA calculated", 200

    @app.route('/calculate_macd', methods=['POST'])
    def calculate_macd():
        """Calculate the MACD and return a success message."""
        utility.calculate_macd()
        return "MACD calculated", 200

    @app.route('/plot_data', methods=['GET'])
    def plot_data():
        """Plot the data and return the plot as a base64 encoded image."""
        utility.plot_data()
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.plot(utility.get_data().index, utility.get_data()['Close'], label='Close Price')
        axis.plot(utility.get_data().index, utility.get_data()['SMMA'], label='SMMA')
        axis.plot(utility.get_data().index, utility.get_data()['MACD'], label='MACD')
        axis.plot(utility.get_data().index, utility.get_data()['MACD_Signal'], label='MACD Signal')
        axis.legend()

        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return base64.b64encode(output.getvalue()).decode('utf-8')

    app.run(host='0.0.0.0', port=5000)