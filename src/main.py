from flask import Flask, render_template
import os
import yaml

DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1', 't', 'yes', 'y')
PORT = 9000
DATA_DIR = os.getenv('DATA_DIR', './data')
OPEN_IN_NEW_TAB = os.getenv('OPEN_IN_NEW_TAB', 'True').lower() in ('true', '1', 't', 'yes', 'y')
TITLE = os.getenv('TITLE', 'LaC - Links as Code')

app = Flask(__name__)

@app.route('/')
def index():
    # Load the first YAML file in DATA_DIR
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(os.path.join(DATA_DIR, filename), 'r') as f:
                links = yaml.safe_load(f)
            break
    else:
        return "No YAML files found in data directory.", 404
        
    return render_template('index.html', data=links, open_in_new_tab=OPEN_IN_NEW_TAB, title=TITLE)


if __name__ == '__main__':
    if DEBUG:
        app.run(debug=DEBUG, port=PORT, host='0.0.0.0')
    else:
        from waitress import serve
        serve(app, port=PORT)