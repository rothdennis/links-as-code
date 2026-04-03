from flask import Flask, render_template
import os
import yaml

DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1', 't', 'yes', 'y')
PORT = 5050
DATA_DIR = os.getenv('DATA_DIR', './data')

app = Flask(__name__)

@app.route('/')
def index():
    # Load the first YAML file in DATA_DIR
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(os.path.join(DATA_DIR, filename), 'r') as f:
                links = yaml.safe_load(f)
            break
    return render_template('index.html', data=links)


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host='0.0.0.0')