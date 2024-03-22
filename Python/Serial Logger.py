import serial
import serial.tools.list_ports



def list_available_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = []
    for port, desc, hwid in sorted(ports):
        available_ports.append((port, desc, hwid))
    return available_ports

print(list_available_ports())
serial_port = str(input("Select COM Port"))  # Update with your serial port
baud_rate = 3000000  # Update with your baud rate
log_file = 'output.log'

ser = serial.Serial(serial_port, baud_rate)

with open(log_file, 'wb') as f:
    while True:
        data = ser.read(ser.in_waiting or 1)
        f.write(data)