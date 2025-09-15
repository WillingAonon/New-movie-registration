## 🎬 MINI PROJECT: New-Movie-Registration


โปรเจกต์นี้เป็นแอปฯจัดการรายชื่อหนังสำหรับทีมของเราในการเรียนรู้และลงมือทำจริงใน 3 เรื่องหลัก:
1.  **Agile & Scrum:** บริหารโปรเจกต์เป็น Sprint สั้นๆ เพื่อส่งมอบงานอย่างรวดเร็ว
2.  **Git Flow:** ฝึกฝนการทำงานร่วมกันบน Git & GitHub อย่างมืออาชีพผ่าน Branch, Pull Request, และ Code Review
3.  **Teamwork:** แบ่งบทบาทชัดเจน (Planner, Coder, Debugger) เพื่อเรียนรู้ความรับผิดชอบในแต่ละตำแหน่ง

---
## 🛠️ เทคโนโลยีที่ใช้ (Tech Stack)

- **Backend:** Python, Flask
- **Deployment:** Docker

---
## 🚀 วิธีการรันโปรเจกต์ (How to Run)

**สิ่งที่ต้องมีก่อน (Prerequisites):**
-   ต้องติดตั้ง [Python 3](https://www.python.org/downloads/) บนเครื่องของคุณ
- ต้องติดตั้ง [Docker Desktop](https://www.docker.com/products/docker-desktop/) บนเครื่องคอมพิวเตอร์

**ขั้นตอนการรัน:**

1.  **Clone a Repository**
    ```bash
    git clone https://github.com/WillingAonon/New-movie-registration.git
    cd New-movie-registration
    ```

2.  **Build Docker Image**
    ใช้คำสั่งนี้ใน Terminal เพื่อสร้าง Image จาก `Dockerfile`
    ```bash
    docker build -t movie-api .
    ```

3.  **Run Docker Container**
    รันคำสั่งนี้เพื่อเปิดใช้งาน API ของเรา
    ```bash
    docker run -p 5000:5000 -v "$(pwd)":/app --name my-movie-app movie-api
    ```
    - คำสั่งนี้จะเชื่อม Port 5000 ของเครื่องคุณเข้ากับ Docker และเชื่อมโฟลเดอร์โปรเจกต์ทั้งหมดของคุณเข้าไป ทำให้ข้อมูลใน `movies.json` ไม่หายไปไหน

4.  **API ก็พร้อมใช้งานแล้ว!**
    คุณสามารถเข้าถึง API ได้ที่ `http://localhost:5000`

---

## 🔌 ตัวอย่างการใช้งาน API (API Endpoints)

คุณสามารถทดสอบ API ได้โดยใช้ `curl` ใน Terminal หรือโปรแกรมอย่าง Postman

#### 1. ดูหนังทั้งหมด (GET)
```bash
curl http://localhost:5000/movies
```
#### 2. เพิ่มหนังใหม่ (POST)
```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "Inception", "year": 2010, "genre": "Sci-Fi"}' http://localhost:5000/movies
```
#### 3. ลบหนัง (DELETE)
```bash
curl -X DELETE http://localhost:5000/movies/Inception
```
---

## 🎯 Current Sprint: Week 3 - API & Docker

**สถานะ:** 🚧 In Progress

### Features

- **REST API:** มี API สำหรับจัดการข้อมูลหนังครบทุกฟังก์ชันพื้นฐาน
  - `GET /movies`: ดูรายชื่อหนังทั้งหมด
  - `POST /movies`: เพิ่มหนังเรื่องใหม่
  - `DELETE /movies/<title>`: ลบหนังตามชื่อเรื่อง
- **Persistent Data:** ข้อมูลหนังจะถูกบันทึกลงในไฟล์ `movies.json` และข้อมูลจะไม่หายไปเมื่อปิดและเปิดโปรแกรมใหม่
- **Dockerized:** โปรแกรมทั้งหมดถูกบรรจุ (Containerized) ด้วย Docker ทำให้ง่ายต่อการติดตั้งและรันโปรแกรมในทุกสภาพแวดล้อม

### Our Team

| Role | Name |
| :--- | :--- |
| 🗺️ **Planner / Architect** | อ้น |
| 💻 **Coder / Builder** | เนย |
| 🕵️‍♀️ **Debugger / Finisher**| รักบี้ |

### Definition of Done (DoD)
- [ ] API ต้องทำงานได้ครบทั้ง 3 endpoints (GET, POST, DELETE)
- [ ] ข้อมูลต้องถูกบันทึกลง movies.json ได้จริงเมื่อใช้ API
- [ ] โปรเจกต์ต้องสามารถ build เป็น Docker image และรันเป็น container ได้สำเร็จ
- [ ] ข้อมูลต้องไม่หาย หลังจากที่ docker stop แล้ว docker start container ใหม่อีกครั้ง


---

## 🗂️ Project Timeline & Archive

ที่นี่คือบันทึกการเดินทางของโปรเจกต์เรา ทุก Sprint ที่เสร็จสิ้นจะถูกนำมาเก็บไว้ที่นี่

<details>
  <summary>ดู Sprint ที่ผ่านมาได้ที่นี่</summary>
    - Sprint1 --> https://colab.research.google.com/drive/1pVw00W_V8-Bh3_8rUnJChns-YXG9EFqb?usp=sharing  <br>
    - Sprint2 --> https://colab.research.google.com/drive/1dLIIZpdkclgA2_gmWdY7rh9lKxXsNTK8?usp=sharing  <br>
    - Sprint3 --> https://colab.research.google.com/drive/1eYIYz7Owcdhx15ZTFxD8gIbDk2tZEUs8?usp=sharing

  </details>
