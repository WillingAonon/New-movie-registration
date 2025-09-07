import json
import os

# ชื่อไฟล์สำหรับเก็บข้อมูลหนัง
FILENAME = "movies.json"

def load_movies():
    """โหลดข้อมูลหนังจากไฟล์ JSON ถ้ามี"""
    if not os.path.exists(FILENAME):
        return []  # ถ้าไฟล์ยังไม่มี คืนลิสต์ว่าง
    
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            # กรณีไฟล์ว่าง
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        # กรณีไฟล์เสียหายหรือไม่เจอ
        return []

def save_movies(movies):
    """บันทึกข้อมูลหนังทั้งหมดลงไฟล์ JSON"""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        # ใช้ indent=4 เพื่อให้อ่านง่าย
        json.dump(movies, f, indent=4)

def run_movie_cli():
    """ฟังก์ชันหลักสำหรับรัน Movie Registration CLI"""
    movies = load_movies()

    print("--- Welcome to Movie Registration CLI ---")
    print("Available commands: [add, view, find, delete, quit]")

    while True:
        command = input("\nEnter command: ").lower().strip()

        # เพิ่ม genre ตอนเพิ่มหนัง
        if command == 'add':
            title = input("Enter movie title: ")
            
            while True:
                year_str = input("Enter release year: ")
                if year_str.isdigit():
                    year = int(year_str)
                    break
                else:
                    print("Error: Invalid year. Please enter a number.")
            
            genre = input("Enter genre (e.g., Action, Comedy, Sci-Fi): ")
            # สร้าง dictionary ของหนังใหม่
            new_movie = {'title': title, 'year': year, 'genre': genre}
            movies.append(new_movie)
            save_movies(movies)
            
            print(f"Success: '{title}' ({year}) - Genre: {genre} has been added.")
            
        # แสดงหนัง พร้อม genre
        elif command == 'view':
            print("\n--- Movie List ---")
            if not movies:
                print("The movie list is empty.")
            else:
                for index, movie in enumerate(movies, start=1):
                    genre = movie.get('genre', 'N/A') 
                    print(f"{index}. {movie['title']} ({movie['year']}) - Genre: {genre}")
        
        # ค้นหาหนัง พร้อม genre
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

        # ลบหนัง
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

        # ออกจากโปรแกรม
        elif command == 'quit':
            print("--- Thank you for using the service! ---")
            break

        else:
            print(f"Error: Unknown command '{command}'. Please try again.")

if __name__ == "__main__":
    run_movie_cli()