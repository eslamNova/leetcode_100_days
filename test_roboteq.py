import serial
import time

# Open the serial connection
ser = serial.Serial(
    port='COM1',  # or 'COMx' for Windows, change to the correct port
    baudrate=115200,
    timeout=1
)

# Send a command to set motor speed
while True:
    
    ser.write(b'!G 1 1000\r')

    # Read the response (if any)
    time.sleep(0.1)
    response = ser.readline().decode('utf-8')
    print(f"Received: {response}")
    time.sleep(0.1)

# Close the connection
ser.close()
