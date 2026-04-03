# LaC (Links as Code)

## Development environment setup

```sh
# Create a virtual environment
python3 -m venv .venv
# Activate the virtual environment
source .venv/bin/activate
# Update pip
pip install --upgrade pip
# Install dependencies
pip install -r requirements.txt
```

```sh
# Run tailwindcss in watch mode
./tailwindcss -i ./src/static/input.css -o ./src/static/style.css --watch
```

```sh
# Start the Flask application
python src/app.py
```