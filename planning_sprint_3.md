# 📝 Planning Sprint 3 – New Movie Registration

## 🎯 เป้าหมายของ Sprint 3

- **REST API:** มี API ที่ทำงานได้อย่างสมบูรณ์สำหรับ GET (ดู), POST (เพิ่ม), และ DELETE (ลบ) ข้อมูลหนัง  
- **Persistent Data:** ข้อมูลถูกเก็บในไฟล์ `movies.json` ที่อยู่นอก Container ทำให้ข้อมูลไม่สูญหายเมื่อ Container หยุดทำงาน  
- **Dockerized Application:** โปรแกรมทั้งหมดถูกบรรจุอยู่ใน Docker Image ทำให้สามารถนำไปรันที่เครื่องไหนก็ได้ที่มี Docker ติดตั้งอยู่ ด้วยคำสั่งเพียงไม่กี่ขั้นตอน  

---

## ✅ Definition of Done (DoD)

- API ต้องทำงานได้ครบทั้ง 3 endpoints (GET, POST, DELETE)  
- ข้อมูลต้องถูกบันทึกลง `movies.json` ได้จริงเมื่อใช้ API  
- โปรเจกต์ต้องสามารถ build เป็น Docker image และรันเป็น container ได้สำเร็จ  
- ข้อมูลต้องไม่หาย หลังจากที่ `docker stop` แล้ว `docker start` container ใหม่อีกครั้ง  

---

## 🧪 Test Cases (กรณีทดสอบ)

### Test Case 10: การเพิ่มข้อมูลผ่าน API (POST)
1. รัน container ด้วย Docker  
2. ใช้คำสั่ง `curl -X POST` ส่งข้อมูลหนังใหม่ เช่น `{ "title": "Inception", "year": 2010 }`  
**ผลลัพธ์ที่คาดหวัง:** ได้สถานะ `201 Created` และข้อมูลถูกเพิ่มลงใน `movies.json`  

---

### Test Case 11: การเพิ่มข้อมูลไม่สมบูรณ์ (POST Invalid)
1. รัน container ด้วย Docker  
2. ใช้คำสั่ง `curl -X POST` ส่งข้อมูลไม่ครบ เช่น `{ "title": "Inception" }`  
**ผลลัพธ์ที่คาดหวัง:** ได้สถานะ `400 Bad Request` พร้อมข้อความแจ้งข้อผิดพลาด  

---

### Test Case 12: การลบข้อมูลที่มีอยู่จริง (DELETE)
1. รัน container และเพิ่มหนังไว้ล่วงหน้า  
2. ใช้คำสั่ง `curl -X DELETE` เพื่อลบหนังที่มีอยู่  
**ผลลัพธ์ที่คาดหวัง:** สถานะ `200 OK` และหนังถูกลบออกจาก `movies.json`  

---

### Test Case 13: การลบข้อมูลที่ไม่มีอยู่ (DELETE Non-existent)
1. รัน container ด้วย Docker  
2. ใช้คำสั่ง `curl -X DELETE` เพื่อลบหนังที่ไม่มีอยู่ในระบบ  
**ผลลัพธ์ที่คาดหวัง:** ได้สถานะ `404 Not Found` หรือข้อความแจ้งข้อผิดพลาด  

---

### Test Case 14: การดูข้อมูลทั้งหมด (GET)
1. รัน container ด้วย Docker  
2. ใช้คำสั่ง `curl http://localhost:5000/movies`  
**ผลลัพธ์ที่คาดหวัง:** ได้รายการหนังทั้งหมดใน `movies.json`  

---

### Test Case 15: Data Persistence (ทดสอบการไม่หายของข้อมูล)
1. รัน container และเพิ่มข้อมูลลงไป  
2. ใช้ `docker stop my-movie-app`  
3. ใช้ `docker start my-movie-app`  
4. เปิด `http://localhost:5000/movies`  
**ผลลัพธ์ที่คาดหวัง:** ข้อมูลที่เคยเพิ่มยังคงอยู่ ไม่ถูกรีเซ็ต  

---

## 🛠️ ขั้นตอนการทดสอบ Docker

1. Build image:
```bash
docker build -t movie-api .
```

2. Run container พร้อม mount ไฟล์ `movies.json`:
```bash
docker run -p 5000:5000 -v "$(pwd)/movies.json:/app/movies.json" --name my-movie-app movie-api
```

3. ใช้ `curl` หรือเบราว์เซอร์ทดสอบ API ตาม Test Case ข้างต้น  

---

## 👥 บทบาททีม

- **อ้น (Planner):** ตรวจสอบ DoD, จัดลำดับงาน, เตรียม test cases  
- **เนย (Coder):** เขียน API + Dockerfile + Docker Compose  
- **รักบี้ (Debugger):** ทดสอบทุกเคส, แก้บั๊ก, ยืนยัน persistence และ compatibility  
