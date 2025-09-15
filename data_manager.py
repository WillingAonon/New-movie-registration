import json
import os

FILENAME = "movies.json"

def load_movies():
    """โหลดข้อมูลหนังจากไฟล์ JSON ถ้ามี"""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_movies(movies):
    """บันทึกข้อมูลหนังทั้งหมดลงไฟล์ JSON"""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(movies, f, indent=4)