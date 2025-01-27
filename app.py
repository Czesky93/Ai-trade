
from flask import Flask, render_template, jsonify
import numpy as np
from modules.ai_strategy import AIStrategy

app = Flask(__name__)

# AI strategy instance
ai_strategy = AIStrategy()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai_dashboard')
def ai_dashboard():
    return render_template('ai_dashboard.html')

@app.route('/ai_analysis')
def ai_analysis():
    # Mock data for AI analysis
    historical_data = np.random.rand(100) * 100  # 100 random prices
    current_price = np.random.rand(1)[0] * 100
    analysis = ai_strategy.analyze_market(historical_data, current_price)
    return jsonify(analysis)

if __name__ == "__main__":
    app.run(debug=True)
