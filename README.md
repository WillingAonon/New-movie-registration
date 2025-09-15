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
    python New Movie Registration.py
    ```
    ...and the CLI is now running!

---

## 🧑‍💻 Our Team

| Role | Name |
| :--- | :--- |
| 🗺️ **Planner / Architect** | เนย |
| 💻 **Coder / Builder** | รักบี้ |
| 🕵️‍♀️ **Debugger / Finisher**| อ้น |

---

## 🎯 Sprint1: Week 1 - สร้างโครงสร้างหลักของโปรแกรม

**สถานะ:** 🚧 ✅

เป้าหมายหลักของสัปดาห์นี้คือการสร้างโปรแกรมผ่าน Command-Line (CLI) ที่เรียบง่ายแต่ทำงานได้จริง เมื่อจบสัปดาห์ โปรแกรมควรจะสามารถ:
- แสดงข้อความต้อนรับและคำสั่งที่ใช้งานได้
- **Add**: เพิ่มหนังเรื่องใหม่ (พร้อมชื่อเรื่องและปีที่ฉาย) เข้าไปในลิสต์ได้
- **View**: ดูรายชื่อหนังทั้งหมดที่ถูกเพิ่มเข้ามาได้
- **Quit**: ออกจากโปรแกรมได้อย่างถูกต้อง

### Definition of Done (DoD)   
- ✅ โปรแกรมสามารถรันได้โดยไม่เกิดข้อผิดพลาด (Error)
- ✅ คำสั่ง `add` สามารถบันทึกชื่อเรื่องและปีของหนังเรื่องใหม่ได้อย่างถูกต้อง
- ✅ คำสั่ง `view` แสดงรายชื่อหนังทั้งหมดพร้อมลำดับเลข
- ✅ คำสั่ง `view` แสดงข้อความว่าลิสต์ว่างเปล่า หากยังไม่มีหนัง
- ✅ คำสั่ง `quit` ทำให้โปรแกรมปิดตัวลงอย่างสมบูรณ์
- ✅ ทุกคำสั่ง (`add`, `view`, `quit`) ไม่ต้องสนใจตัวพิมพ์เล็ก/ใหญ่ (เช่น พิมพ์ `ADD` หรือ `Add` ก็ต้องทำงานได้)
- ✅ เมื่อพิมพ์คำสั่งที่ไม่มีอยู่จริง โปรแกรมต้องแสดงข้อความผิดพลาดและให้ผู้ใช้ลองใหม่อีกครั้ง

---

## 🎯 Current Sprint: Week 2 - ทำให้โปรแกรมจำข้อมูลและจัดการข้อมูลได้

**สถานะ:** 🚧 ✅

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
- [ ] โปรแกรมสามารถโหลดข้อมูลจากไฟล์ `movies.json` ตอนเริ่มต้นได้
- [ ] คำสั่ง `delete` สามารถลบหนังออกจากลิสต์และอัปเดตไฟล์ได้ถูกต้อง
- [ ] คำสั่ง `find` สามารถค้นหาหนังเจอและไม่เจอได้อย่างถูกต้อง
- [ ] เมื่อป้อน "ปีที่ฉาย" ที่ไม่ใช่ตัวเลข โปรแกรมต้องแสดงข้อความผิดพลาดและไม่หยุดทำงาน
- [ ] ข้อมูลหนังยังคงอยู่ครบถ้วน แม้จะปิดแล้วเปิดโปรแกรมใหม่

---

## 🗂️ Project Timeline & Archive

ที่นี่คือบันทึกการเดินทางของโปรเจกต์เรา ทุก Sprint ที่เสร็จสิ้นจะถูกนำมาเก็บไว้ที่นี่

<details>
  <summary>ดู Sprint ที่ผ่านมาได้ที่นี่</summary>
    - Sprint1 --> https://colab.research.google.com/drive/1pVw00W_V8-Bh3_8rUnJChns-YXG9EFqb?usp=sharing  <br>
    - Sprint2 --> https://colab.research.google.com/drive/1dLIIZpdkclgA2_gmWdY7rh9lKxXsNTK8?usp=sharing  <br>
    - Sprint3 -->

  </details>
