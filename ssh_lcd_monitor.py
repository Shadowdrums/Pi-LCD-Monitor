import time
import subprocess
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import psutil

lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
              numbering_mode=GPIO.BOARD,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True)

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

def ssh_users():
    cmd = "who | grep 'pts' | awk '{print $1}'"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    users = output.decode('utf-8').strip().split('\n')
    return users

try:
    while True:
        users = ssh_users()
        if users and users[0]:  
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string('SSH Users:')
            lcd.cursor_pos = (1, 0)
            lcd.write_string(','.join(users)[:16])
        else:
            lcd.clear()
            temp = get_cpu_temperature()
            used_ram, total_ram = get_ram_usage()
            lcd.cursor_pos = (0, 0)
            lcd.write_string(f'Temp: {temp:.1f}C')
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f'RAM:{used_ram}G/{total_ram}G')
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    GPIO.cleanup()
