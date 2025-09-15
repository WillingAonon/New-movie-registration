# --- Stage 1: เลือก Base Image ---
# เริ่มต้นจาก official image ของ Python เวอร์ชัน 3.9 แบบ slim
# ซึ่งมีขนาดเล็กและเหมาะสำหรับ production
FROM python:3.9-slim

# --- Stage 2: ตั้งค่า Environment ---
# ตั้งค่า Working Directory ภายใน Container เป็น /app
# คำสั่งทั้งหมดหลังจากนี้จะทำงานใน directory นี้
WORKDIR /app

# --- Stage 3: ติดตั้ง Dependencies ---
# คัดลอกเฉพาะไฟล์ requirements.txt เข้าไปก่อน
# Docker จะ cache layer นี้ไว้ ถ้าไฟล์นี้ไม่เปลี่ยน การ build ครั้งถัดไปจะเร็วขึ้นมาก
COPY requirements.txt .

# รันคำสั่ง pip install เพื่อติดตั้ง library ที่ระบุใน requirements.txt
# --no-cache-dir ช่วยให้ image มีขนาดเล็กลง
RUN pip install --no-cache-dir -r requirements.txt

# --- Stage 4: คัดลอก Source Code ---
# คัดลอกไฟล์ทั้งหมดในโปรเจกต์ ( . ) เข้าไปใน Working Directory ของ container ( . )
COPY . .

# --- Stage 5: กำหนดค่า Network และคำสั่งเริ่มต้น ---
# บอกให้ Docker รู้ว่า Container ของเราจะทำงานที่ Port 5000
EXPOSE 5000

# คำสั่งที่จะรันเมื่อ Container เริ่มทำงาน
# ในที่นี้คือการสั่งให้ python รันไฟล์ api.py
CMD ["python", "api.py"]