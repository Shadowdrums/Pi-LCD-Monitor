import time
import subprocess
import psutil
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
from datetime import timedelta

# Initialize LCD
lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
              numbering_mode=GPIO.BOARD,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True)

# Functions to Retrieve System Information
def get_cpu_temperature():
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
            temp = float(file.read()) / 1000.0
            return temp
    except FileNotFoundError:
        return None

def get_ram_usage():
    memory = psutil.virtual_memory()
    used_gb = round(memory.used / (1024 ** 3), 2)
    total_gb = round(memory.total / (1024 ** 3), 2)
    return used_gb, total_gb

def get_storage_info():
    storage = psutil.disk_usage("/")
    used_gb = round(storage.used / (1024 ** 3), 2)
    total_gb = round(storage.total / (1024 ** 3), 2)
    return used_gb, total_gb

def get_ip_address():
    try:
        cmd = "hostname -I | awk '{print $1}'"
        return subprocess.getoutput(cmd)
    except:
        return "Unavailable"

def get_system_uptime():
    try:
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_str = str(timedelta(seconds=uptime_seconds))
            return uptime_str.split(".")[0]  # Ignore milliseconds
    except:
        return "Unavailable"

def ssh_users():
    cmd = "who | grep 'pts' | awk '{print $1}'"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    users = output.decode('utf-8').strip().split('\n')
    return users

def get_info_pairs():
    temp = get_cpu_temperature()
    cpu_usage = f"{psutil.cpu_percent()}%"
    used_ram, total_ram = get_ram_usage()
    uptime = get_system_uptime()
    used_storage, total_storage = get_storage_info()
    ip_address = get_ip_address()
    
    return [
        (f"Temp: {temp:.1f}C", f"CPU Usage: {cpu_usage}"),
        (f"RAM: {used_ram}/{total_ram}G", f"Uptime: {uptime}"),
        (f"IP: {ip_address}", f"Stor: {used_storage}/{total_storage}G")
    ]

def update_lcd_smooth(lines, previous_lines):
    transition_steps = 16
    for i in range(transition_steps + 1):
        transition_line1 = previous_lines[0][i:] + lines[0][:i]
        transition_line2 = previous_lines[1][i:] + lines[1][:i]
        
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(transition_line1.ljust(16))
        lcd.cursor_pos = (1, 0)
        lcd.write_string(transition_line2.ljust(16))
        time.sleep(0.2)  # Time per transition step

try:
    pair_index = 0
    previous_lines = ("", "")
    
    while True:
        users = ssh_users()
        info_pairs = get_info_pairs()
        
        if users and users[0]:  # Users are connected via SSH
            line1 = "Active SSH Users:"
            line2 = users[pair_index % len(users)]  
        else:  # No SSH users, show system info
            line1, line2 = info_pairs[pair_index % len(info_pairs)]  

        update_lcd_smooth((line1, line2), previous_lines)
        previous_lines = (line1, line2)

        pair_index += 1
        time.sleep(10 - 0.2 * 16)  # Static display time for each pair
        
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    GPIO.cleanup()
