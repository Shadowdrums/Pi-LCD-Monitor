# 🚀 Pi-LCD-Monitor 

> **Elegantly monitor CPU temperature, RAM usage, and SSH users on a 16x2 LCD with your Raspberry Pi 4!**

---

## 🎯 Overview 

**Pi-LCD-Monitor** provides a concise and interactive dashboard that elegantly exhibits vital system information and user access data on a 16x2 LCD connected to your Raspberry Pi. 

Delve into real-time details like:
- 🧑‍💻 Active SSH user names
- 🌡️ CPU temperature
- 💾 RAM usage
- 🔄 System uptime
- 🌐 IP Address
- 📦 Storage info

Ensuring seamless understanding of system health and secure usage.

---

## 🏗 About The Project 

### Why Developed

Formulated for the SSH server on Raspberry Pi, aiming to:
- **Monitor SSH Users**: Visualize active SSH sessions in a snapshot.
- **Oversee System Health**: Continually oversee key health metrics without manual probing.
- **Seamless System Monitoring**: Scroll through paired metric info smoothly and readably on the LCD.

### Development Details
- **🍰 Raspberry Pi Model**: 4B 8GB
- **🖥 Operating System**: Kali Linux Purple 64bit 2023.1
- **📟 LCD**: 16x2 Character LCD (Hitachi HD44780)

---

## 🚀 Getting Started 

### 🛠 Prerequisites 

- **🧱 Hardware**: Raspberry Pi 4B, 16x2 LCD, Jump wires, and optionally, a Breadboard.
- **👩‍💻 Software**: Python 3.x installed on Kali Linux.

### 📦 Dependencies 

pip install RPLCD RPi.GPIO psutil

### 🔌 Hardware Connection
[// Hardware connection details as previously mentioned]

### 💻 Usage
Run the script using Python:

python3 /path/to/ssh_lcd_monitor.py

### 🔄 Automated Startup (Optional)
Create a systemd Service File:

sudo nano /etc/systemd/system/sshmonitor.service

### Configure the .Service

[Unit]
Description=SSH and System Info Display

[Service]
ExecStart=/usr/bin/python3 /path/to/ssh_lcd_monitor.py
User=pi
Restart=always

[Install]
WantedBy=multi-user.target

### Enable and Start the Service

sudo systemctl enable sshmonitor
sudo systemctl start sshmonitor

### ✉️ Contributing & Feedback

🌟 Your contributions and feedback are invaluable! Feel free to fork, pull, or open an issue to share your insights and suggestions.

Thank you for exploring Pi-LCD-Monitor! 🎉

### Note:


Please ensure to replace `/path/to/ssh_lcd_monitor.py` with the actual path to your Python script in the Raspberry Pi filesystem. This README can be adjusted as per any additional features or changes you implement in your project moving forward!

