import json
import os

# Define the filename for storing movie data
FILENAME = "movies.json"

def load_movies():
    """Loads movies from the JSON file if it exists."""
    if not os.path.exists(FILENAME):
        return []  # Return an empty list if the file doesn't exist yet
    
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            # Handle empty file case
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        # Handle cases where the file is empty or corrupted
        return []

def save_movies(movies):
    """Saves the entire movie list to the JSON file."""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        # Use indent=4 for a pretty, readable JSON file
        json.dump(movies, f, indent=4)

def run_movie_cli():
    """Main function to run the Movie Registration CLI."""
    movies = load_movies()

    print("--- Welcome to Movie Registration CLI ---")
    print("Available commands: [add, view, find, delete, quit]")

    while True:
        command = input("\nEnter command: ").lower().strip()

        # === 🚀 UPGRADE POINT 1: ADD COMMAND NOW ASKS FOR GENRE ===
        if command == 'add':
            title = input("Enter movie title: ")
            
            while True:
                year_str = input("Enter release year: ")
                if year_str.isdigit():
                    year = int(year_str)
                    break
                else:
                    print("Error: Invalid year. Please enter a number.")
            
            # --- ADDED THIS LINE ---
            genre = input("Enter genre (e.g., Action, Comedy, Sci-Fi): ")
            # ---------------------

            # Add 'genre' to the new_movie dictionary
            new_movie = {'title': title, 'year': year, 'genre': genre}
            movies.append(new_movie)
            save_movies(movies)
            
            print(f"Success: '{title}' ({year}) - Genre: {genre} has been added.")
            
        # === 🚀 UPGRADE POINT 2: VIEW COMMAND NOW SHOWS GENRE ===
        elif command == 'view':
            print("\n--- Movie List ---")
            if not movies:
                print("The movie list is empty.")
            else:
                for index, movie in enumerate(movies, start=1):
                    # Use .get() to avoid errors if old movies don't have a genre
                    genre = movie.get('genre', 'N/A') 
                    print(f"{index}. {movie['title']} ({movie['year']}) - Genre: {genre}")
        
        # === 🚀 UPGRADE POINT 3: FIND COMMAND NOW SHOWS GENRE ===
        elif command == 'find':
            search_title = input("Enter movie title to find: ")
            found_movies = [
                movie for movie in movies 
                if search_title.lower() in movie['title'].lower()
            ]
            
            if not found_movies:
                print(f"Error: Movie containing '{search_title}' not found.")
            else:
                print(f"\n--- Found {len(found_movies)} Movie(s) ---")
                for movie in found_movies:
                    genre = movie.get('genre', 'N/A')
                    print(f"- {movie['title']} ({movie['year']}) - Genre: {genre}")

        elif command == 'delete':
            search_title = input("Enter the exact movie title to delete: ")
            
            original_movie_count = len(movies)
            movies = [
                movie for movie in movies 
                if movie['title'].lower() != search_title.lower()
            ]

            if len(movies) < original_movie_count:
                save_movies(movies)
                print(f"Success: Movie '{search_title}' has been deleted.")
            else:
                print(f"Error: Movie '{search_title}' not found.")

        elif command == 'quit':
            print("--- Thank you for using the service! ---")
            break

        else:
            print(f"Error: Unknown command '{command}'. Please try again.")

if __name__ == "__main__":
    run_movie_cli()