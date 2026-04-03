from flask import Flask, render_template
import os
import yaml

DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1', 't', 'yes', 'y')
PORT = 5050
FILE_PATH = os.getenv('FILE_PATH', './data/links.yaml')

app = Flask(__name__)

@app.route('/')
def index():
    with open(FILE_PATH, 'r') as file:
        links = yaml.safe_load(file)
    return render_template('index.html', data=links)


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host='0.0.0.0')