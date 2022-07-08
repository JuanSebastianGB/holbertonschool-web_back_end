#!/usr/bin/env python3

""" Entry point for the application. """

from flask import Flask, render_template
from os import getenv

app = Flask(__name__)


@app.route('/')
def index():
    """
    The function `index()` returns the rendered template `index.html`
    :return: The index.html file is being returned.
    """

    return render_template('index.html')


if __name__ == "__main__":
    """ This is a common Python idiom to check if the file
    is being run as a script or imported as a module."""
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
