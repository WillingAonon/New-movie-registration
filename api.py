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
    except (json.JSONDecodeError, FileNotFoundError):
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
    
    # ตรวจสอบว่ามีหนังชื่อนี้อยู่แล้วหรือไม่ (ป้องกันการเพิ่มข้อมูลซ้ำ)
    if any(movie['title'].lower() == new_movie['title'].lower() for movie in movies):
        return jsonify({"error": f"Movie with title '{new_movie['title']}' already exists"}), 409

    movies.append(new_movie)
    save_movies(movies)
    return jsonify(new_movie), 201


# --- ส่วนที่แก้ไข ---
# เปลี่ยนจาก <int:movie_id> เป็น <string:title>
@app.route("/movies/<string:title>", methods=["DELETE"])
def delete_movie(title):
    movies = load_movies()
    
    # ค้นหาหนังจาก 'title' แทนการใช้ index
    movie_to_delete = next((movie for movie in movies if movie["title"] == title), None)
    
    if movie_to_delete:
        movies.remove(movie_to_delete) # ลบหนังที่เจอออกจาก list
        save_movies(movies)
        return jsonify({"message": f"Movie '{title}' deleted successfully"}), 200
    
    return jsonify({"error": "Movie not found"}), 404
# --- สิ้นสุดส่วนที่แก้ไข ---


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)