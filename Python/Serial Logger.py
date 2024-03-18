import serial

serial_port = 'COM4'  # Update with your serial port
baud_rate = 3000000  # Update with your baud rate
log_file = 'output.log'

ser = serial.Serial(serial_port, baud_rate)

with open(log_file, 'wb') as f:
    while True:
        data = ser.read(ser.in_waiting or 1)
        f.write(data)