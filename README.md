# Simple Structured Flask App
An easy basic flask app with just enough structure to be a useful starting point.

# Requirements
* Flask 3.x
* Ruff

# Dev Setup
* `python3.12 -m venv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `cp instance/examples/config.toml instance/config.toml`
* `flask run`

# Ruff Usage
Config in: `ruff.toml`

* `ruff check .`
* `ruff format .`
