## 🎬 MINI PROJECT: New-Movie-Registration


โปรเจกต์นี้เป็นแอปฯจัดการรายชื่อหนังสำหรับทีมของเราในการเรียนรู้และลงมือทำจริงใน 3 เรื่องหลัก:
1.  **Agile & Scrum:** บริหารโปรเจกต์เป็น Sprint สั้นๆ เพื่อส่งมอบงานอย่างรวดเร็ว
2.  **Git Flow:** ฝึกฝนการทำงานร่วมกันบน Git & GitHub อย่างมืออาชีพผ่าน Branch, Pull Request, และ Code Review
3.  **Teamwork:** แบ่งบทบาทชัดเจน (Planner, Coder, Debugger) เพื่อเรียนรู้ความรับผิดชอบในแต่ละตำแหน่ง

---
## 🛠️ เทคโนโลยีที่ใช้ (Tech Stack)

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Deployment:** Docker, Docker Compose

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

2.  **Run the application:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the application:**
    - เปิดเว็บเบราว์เซอร์แล้วไปที่ `http://localhost:5000`

---




## 🎯 Current Sprint: Final Sprint

**สถานะ:** ✅ 

### Sprint Final (Goal)
เป้าหมายหลักของเราคือ **"การเปลี่ยน Web Service หลังบ้านให้กลายเป็นเว็บแอปพลิเคชันเต็มรูปแบบ (Full-Stack Web Application) ที่ผู้ใช้ทั่วไปสามารถใช้งานได้จริงผ่านหน้าเว็บ และมีกระบวนการทำงานที่เป็นมาตรฐาน"** โดยมีเป้าหมายย่อยดังนี้:
1. **พัฒนาส่วนติดต่อผู้ใช้ (Web GUI):** สร้างหน้าเว็บเพื่อให้ผู้ใช้สามารถจัดการข้อมูลหนังได้ง่ายขึ้น ไม่ต้องใช้ `curl` ผ่าน command line อีกต่อไป
2. **ปรับปรุงฟังก์ชัน API:** เพิ่มความสามารถให้ API สามารถจัดเก็บข้อมูล **"รอบฉาย" (Showtimes)** ได้
3. **ทำให้การรันโปรเจกต์ง่ายขึ้น:** เปลี่ยนจากการใช้คำสั่ง `docker run` ที่ซับซ้อน มาใช้ `docker-compose` เพื่อให้ใครก็สามารถรันโปรเจกต์ได้ด้วยคำสั่งเดียว

### Our Team

| Role | Name |
| :--- | :--- |
| 🗺️ **Planner / Architect** | เนย|
| 💻 **Coder / Builder** | รักบี้ |
| 🕵️‍♀️ **Debugger / Finisher**| อ้น |

### ✅ Definition of Done (DoD)
เราจะถือว่า Sprint Final นี้สำเร็จลุล่วง เมื่อผ่านเกณฑ์ทั้งหมดต่อไปนี้:
* **[✔] แอปพลิเคชันทำงานได้ครบถ้วน:** ผู้ใช้สามารถ เพิ่ม, ดู, ลบ, และค้นหาข้อมูลภาพยนตร์ผ่านหน้า Web GUI ได้อย่างสมบูรณ์
* **[✔] รันได้ด้วยคำสั่งเดียว:** โปรเจกต์ทั้งหมดสามารถเริ่มทำงานได้ด้วยคำสั่ง `docker-compose up`
* **[✔] ข้อมูลถูกบันทึกอย่างถูกต้อง:** การเพิ่มหรือลบข้อมูลผ่านหน้าเว็บ ส่งผลให้ไฟล์ `movies.json` ถูกอัปเดตอย่างถูกต้อง
* **[✔] มีเอกสารประกอบชัดเจน:** ไฟล์ `README.md` อธิบายวิธีการติดตั้งและใช้งานโปรเจกต์ไว้อย่างครบถ้วน

---

## 🗂️ Project Timeline & Archive

ที่นี่คือบันทึกการเดินทางของโปรเจกต์เรา ทุก Sprint ที่เสร็จสิ้นจะถูกนำมาเก็บไว้ที่นี่

<details>
  <summary>ดู Sprint ที่ผ่านมาได้ที่นี่</summary>
    - Sprint1 --> https://colab.research.google.com/drive/1pVw00W_V8-Bh3_8rUnJChns-YXG9EFqb?usp=sharing  <br>
    - Sprint2 --> https://colab.research.google.com/drive/1dLIIZpdkclgA2_gmWdY7rh9lKxXsNTK8?usp=sharing  <br>
    - Sprint3 --> https://colab.research.google.com/drive/1eYIYz7Owcdhx15ZTFxD8gIbDk2tZEUs8?usp=sharing  <br>
    - Sprint final --> https://colab.research.google.com/drive/1sWTUxNHZan7eV8pcwpftVWpjNTOr6BsS?usp=sharing

  </details>
