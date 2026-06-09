import serial
import time
import re

ser = serial.Serial("COM9", 115200, timeout=1)


with open("output.csv", "w") as f:
    try:
        while True:
            raw = ser.read_all().decode("utf-8", errors="ignore")
            for line in raw.strip().splitlines():
                line = re.sub(r"^\d{2}:\d{2}:\d{2}\.\d+ -> ", "", line).strip()
                if line:
                    f.write(",".join(line.split(" | " or " | | ")) + "\n")
                    f.flush()
            time.sleep(5)
    
    finally:
        ser.close()
