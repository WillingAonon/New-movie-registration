def run_movie_cli():
    """ 
    ฟังก์ชันหลักสำหรับรันโปรแกรม Movie Registration CLI 
    มีลูปหลักสำหรับรอรับคำสั่งจากผู้ใช้และประมวลผล 
    """
    # 1. โครงสร้างข้อมูลสำหรับเก็บข้อมูลหนัง (เริ่มต้นเป็นลิสต์ว่าง)
    movies = []

    # 2. แสดงข้อความต้อนรับเมื่อโปรแกรมเริ่มทำงาน
    print("--- Welcome to Movie Registration CLI ---")
    print("Available commands: [add, view, quit]")

    # 3. ลูปหลักของโปรแกรม (ทำงานไปเรื่อยๆ จนกว่าจะสั่ง break)
    while True:
        # รับคำสั่งจากผู้ใช้ และแปลงเป็นตัวพิมพ์เล็กทั้งหมด (.lower())
        command = input("\nEnter command: ").lower()

        # 4. ตรวจสอบและจัดการคำสั่งด้วย if/elif/else
        if command == 'add':
            title = input("Enter movie title: ")
            year = input("Enter release year: ")
            
            # สร้าง Dictionary สำหรับหนังเรื่องใหม่ แล้วเพิ่มเข้าไปในลิสต์
            new_movie = {'title': title, 'year': year}
            movies.append(new_movie)
            
            print(f"Success: '{title}' ({year}) has been added.")

        elif command == 'view':
            print("\n--- Movie List ---")
            if not movies: # ตรวจสอบว่าลิสต์ว่างหรือไม่
                print("The movie list is empty.")
            else:
                # ใช้ enumerate เพื่อสร้างลำดับเลข (เริ่มต้นที่ 1)
                for index, movie in enumerate(movies, start=1):
                    print(f"{index}. {movie['title']} ({movie['year']})")
        
        elif command == 'quit':
            print("--- Thank you for using the service! ---")
            break  # ออกจาก while loop และจบการทำงานของโปรแกรม

        else:
            # กรณีที่ผู้ใช้พิมพ์คำสั่งที่ไม่รู้จัก
            print(f"Error: Unknown command '{command}'. Please try again.")

# บรรทัดมาตรฐานของ Python เพื่อให้แน่ใจว่าฟังก์ชัน run_movie_cli() จะถูกเรียกใช้
# ก็ต่อเมื่อไฟล์นี้ถูกรันโดยตรงเท่านั้น
if __name__ == "__main__":
    run_movie_cli()
