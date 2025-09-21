from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder="static")

FILENAME = "movies.json"


def load_movies():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify(load_movies())


@app.route("/movies", methods=["POST"])
def add_movie():
    new_movie = request.json
    if not new_movie or "title" not in new_movie or "year" not in new_movie or "genre" not in new_movie:
        return jsonify({"error": "Invalid movie data. Required: title, year, genre"}), 400

    if "showtimes" not in new_movie:
        new_movie["showtimes"] = []

    movies = load_movies()
    movies.append(new_movie)
    save_movies(movies)
    return jsonify(new_movie), 201


@app.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    movies = load_movies()
    if 0 <= movie_id < len(movies):
        deleted = movies.pop(movie_id)
        save_movies(movies)
        return jsonify(deleted)
    return jsonify({"error": "Movie not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
