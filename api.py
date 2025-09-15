from flask import Flask, request, jsonify
from data_manager import load_movies, save_movies

app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_movies():
    """ดึงรายการหนังทั้งหมด"""
    movies = load_movies()
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def add_movie():
    """เพิ่มหนังใหม่"""
    new_movie = request.json
    if not new_movie or 'title' not in new_movie or 'year' not in new_movie:
        return jsonify({"error": "Invalid movie data"}), 400

    movies = load_movies()
    movies.append(new_movie)
    save_movies(movies)
    return jsonify(new_movie), 201

@app.route('/movies/<string:title>', methods=['DELETE'])
def delete_movie(title):
    """ลบหนังตามชื่อเรื่อง"""
    movies = load_movies()
    movie_to_delete = None
    for movie in movies:
        if movie['title'].lower() == title.lower():
            movie_to_delete = movie
            break

    if movie_to_delete:
        movies.remove(movie_to_delete)
        save_movies(movies)
        return jsonify({"success": f"Movie '{title}' deleted."}), 200
    else:
        return jsonify({"error": "Movie not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)