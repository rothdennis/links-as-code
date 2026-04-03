# LaC (Links as Code)

## Features

- Manage your links in a simple YAML file
- Organize links into groups
- Easy deployment with Docker
- Clean and minimalistic interface
- Search functionality to quickly find your links
- Responsive design for mobile and desktop
- 100% accessible (according to Google Lighthouse) and keyboard-friendly

## Deployment

```yaml
services:

  lac:
    image: rothdennis/lac:latest
    container_name: lac
    restart: unless-stopped
    ports:
      - "9010:9010"
    volumes:
      - ./data:/app/data
```

```yaml
# ./data/links.yaml
links:
  - name: GitHub
    url: https://www.github.com
    description: Code hosting platform
  - name: Reddit
    url: https://www.reddit.com
    description: Social news aggregation and discussion website

groups:
  - name: Search Engines
    links:
      - name: Google
        url: https://www.google.com
      - name: Bing
        url: https://www.bing.com
      - name: DuckDuckGo
        url: https://duckduckgo.com
  - name: Social Media
    links:
      - name: Facebook
        url: https://www.facebook.com
      - name: Twitter
        url: https://www.twitter.com
      - name: LinkedIn
        url: https://www.linkedin.com
```

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