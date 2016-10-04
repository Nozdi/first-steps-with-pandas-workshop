from flask import (
    Flask,
    jsonify,
)
import pandas as pd

app = Flask(__name__)


@app.route("/movie-titles")
def movie_titles():
    return jsonify(
        { 'error': 'Please implement me! I want here a list of movie titles!'}
    )


@app.route("/worst")
def worst():
    return jsonify(
        { 'error': 'Please implement me! I want here a list of lowest rated movies ever!'}
    )


@app.route("/best-rated/<int:year>")
def best_rated(year):
    return jsonify(
        { 'error': 'Please implement me! I want here list of best rated movies in a given year!'}
    )


if __name__ == "__main__":
    app.run()
