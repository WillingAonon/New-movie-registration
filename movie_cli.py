import csv
from data_manager import load_movies, save_movies

# --- ฟังก์ชันหลักในการจัดการหนัง ---

def add_movie():
    """เพิ่มหนังใหม่เข้าไปในรายการ"""
    movies = load_movies()
    title = input("Enter movie title: ")
    year_input = input("Enter movie year: ")
    genre = input("Enter movie genre: ")

    # ตรวจสอบว่าปีเป็นตัวเลขหรือไม่
    try:
        year = int(year_input)
    except ValueError:
        print("Error: Year must be a number.")
        return

    # ตรวจสอบว่ามีหนังชื่อนี้อยู่แล้วหรือไม่ (ป้องกันข้อมูลซ้ำ)
    for movie in movies:
        if movie['title'].lower() == title.lower():
            print(f"Error: Movie '{title}' already exists.")
            return

    new_movie = {
        "title": title,
        "year": year,
        "genre": genre
    }
    movies.append(new_movie)
    save_movies(movies)
    print(f"Success: Movie '{title}' has been added.")

def view_movies():
    """แสดงรายการหนังทั้งหมดที่มีอยู่"""
    movies = load_movies()
    if not movies:
        print("No movies in the database yet.")
        return

    print("\n--- Movie List ---")
    # จัดเรียงตามชื่อเรื่องเพื่อให้ดูง่าย
    for movie in sorted(movies, key=lambda m: m['title']):
        print(f"- {movie['title']} ({movie['year']}) [{movie['genre']}]")
    print(f"------------------\nTotal movies: {len(movies)}\n")


def find_movie():
    """ค้นหาหนังจากชื่อเรื่อง"""
    movies = load_movies()
    search_term = input("Enter movie title to find: ").lower()
    
    found_movies = [
        movie for movie in movies 
        if search_term in movie['title'].lower()
    ]

    if not found_movies:
        print(f"No movies found matching '{search_term}'.")
        return
    
    print(f"\nFound {len(found_movies)} movie(s):")
    for movie in found_movies:
        print(f"- {movie['title']} ({movie['year']}) [{movie['genre']}]")
    print("")


def delete_movie():
    """ลบหนังออกจากรายการ (พร้อมการยืนยัน)"""
    movies = load_movies()
    search_title = input("Enter the exact movie title to delete: ")
    
    movie_to_delete = None
    movie_index = -1

    # ค้นหาหนังที่ต้องการลบ
    for i, movie in enumerate(movies):
        if movie['title'].lower() == search_title.lower():
            movie_to_delete = movie
            movie_index = i
            break

    if movie_to_delete:
        # ถามเพื่อยืนยันการลบ
        confirm = input(f"Are you sure you want to delete '{movie_to_delete['title']}'? [y/n]: ").lower()
        if confirm == 'y':
            movies.pop(movie_index) # ลบออกจากลิสต์
            save_movies(movies)
            print(f"Success: Movie '{search_title}' has been deleted.")
        else:
            print("Delete canceled.")
    else:
        print(f"Error: Movie '{search_title}' not found.")


# --- ฟังก์ชัน Import/Export สำหรับ Sprint 3 ---

def export_to_csv():
    """ส่งออกข้อมูลหนังไปยัง movies.csv"""
    movies = load_movies()
    if not movies:
        print("No movies to export.")
        return

    try:
        with open('movies.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['title', 'year', 'genre']) # เขียน Header
            for movie in movies:
                writer.writerow([movie['title'], movie['year'], movie['genre']])
        print("Success: Movies have been exported to movies.csv.")
    except IOError as e:
        print(f"Error writing to file: {e}")


def import_from_csv():
    """นำเข้าข้อมูลหนังจาก movies.csv (ป้องกันข้อมูลซ้ำ)"""
    try:
        with open('movies.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            movies = load_movies()
            existing_titles = {m['title'].lower() for m in movies}
            new_movies_count = 0

            for row in reader:
                # ตรวจสอบว่ามีข้อมูลครบทุกคอลัมน์หรือไม่
                if not all(key in row for key in ['title', 'year', 'genre']):
                    print(f"Warning: Skipping invalid row in CSV: {row}")
                    continue

                if row['title'].lower() not in existing_titles:
                    try:
                        movies.append({
                            'title': row['title'],
                            'year': int(row['year']),
                            'genre': row['genre']
                        })
                        existing_titles.add(row['title'].lower()) # เพิ่ม title ใหม่เข้าไปใน set ด้วย
                        new_movies_count += 1
                    except (ValueError, TypeError):
                        print(f"Warning: Skipping row with invalid year '{row['year']}' for movie '{row['title']}'.")
            
            if new_movies_count > 0:
                save_movies(movies)
            
            print(f"Success: Imported {new_movies_count} new movies from movies.csv.")

    except FileNotFoundError:
        print("Error: movies.csv not found. Please create it first or use 'export'.")
    except Exception as e:
        print(f"An unexpected error occurred during import: {e}")


# --- ส่วนของ Command-Line Interface ---

def print_menu():
    """แสดงเมนูคำสั่ง"""
    print("\n===== Movie Registration System =====")
    print("  add    - Add a new movie")
    print("  view   - View all movies")
    print("  find   - Find a movie by title")
    print("  delete - Delete a movie")
    print("  import - Import movies from movies.csv")
    print("  export - Export movies to movies.csv")
    print("  exit   - Exit the program")
    print("=====================================")


def run_movie_cli():
    """ฟังก์ชันหลักสำหรับรันโปรแกรม CLI"""
    while True:
        print_menu()
        command = input("Enter your command: ").lower().strip()

        if command == 'add':
            add_movie()
        elif command == 'view':
            view_movies()
        elif command == 'find':
            find_movie()
        elif command == 'delete':
            delete_movie()
        elif command == 'import':
            import_from_csv()
        elif command == 'export':
            export_to_csv()
        elif command == 'exit':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")


# --- จุดเริ่มต้นการทำงานของโปรแกรม ---
if __name__ == "__main__":
    run_movie_cli()