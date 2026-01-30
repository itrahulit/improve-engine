"""
A simple Flask web application - Sample Website
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')


if __name__ == '__main__':
    # Note: Debug mode is enabled for development/learning purposes.
    # For production deployment, set debug=False and configure proper hosting.
    app.run(debug=True, host='0.0.0.0', port=5000)
