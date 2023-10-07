# Pi-LCD-Monitor
This is for a lcd screen on pi 4 to monitor cpu temp, ram usage and ssh users

# Raspberry Pi SSH Monitor & System Info Display on LCD

Monitor your Raspberry Pi's SSH activity and core system metrics live on a 16x2 LCD!

## Overview

SSH Monitor & System Info Display was developed with the intention of assisting system administrators and hobbyists to visually monitor their Raspberry Pi's SSH access and essential system health parameters in a concise and immediate manner.

Utilizing the **Hitachi HD44780** LCD controller compatible 16x2 LCD, the project provides a straightforward, real-time visualization of:
- Active SSH user names,
- CPU temperature, and
- RAM usage.

## About The Project

### Why Developed
This project was developed for a ssh server, to fulfill a need to:
- **Monitor SSH Users**: Know who is accessing your Raspberry Pi via SSH without command-line checks.
- **Keep an Eye on System Health**: View critical system health metrics at a glance.

### Development Context
- **Raspberry Pi Model**: 4B 8GB
- **Operating System**: Kali Linux Purple 64bit 2023.1
- **LCD**: 16x2 Character LCD with a Hitachi HD44780 controller

## Getting Started

### Prerequisites

Ensure the following components and settings:
- **Hardware**: Raspberry Pi 4B, 16x2 LCD, Jump wires, and optionally, a Breadboard.
- **Software**: Python 3.x installed on Kali Linux.

### Dependencies

Install the required Python libraries using pip:

pip install RPLCD RPi.GPIO psutil

### Hardware Connection
Connect the 16x2 LCD to the Raspberry Pi as per the following configuration:

VSS -> GND
VDD -> 5V
VO -> To a potentiometer (for contrast adjustment)
RS -> GPIO22
RW -> GND
E -> GPIO17
D4 -> GPIO25
D5 -> GPIO24
D6 -> GPIO23
D7 -> GPIO18
A -> 5V (or through a resistor for backlight adjustment)
K -> GND

### Usage
Simply run the script with Python:
python3 /path/to/ssh_lcd_monitor.py

### Automated Startup (Optional)
You may set up the script to run on startup using the systemd service.

Create a systemd Service File

sudo nano /etc/systemd/system/sshmonitor.service

### Configure the Service

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

### Contributing & Feedback
Your contributions and feedback are welcomed! Feel free to fork the project and submit a pull request, or open an issue to share your thoughts and suggestions.
