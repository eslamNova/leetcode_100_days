import pyads

try:
    # Connect to the PLC
    plc = pyads.Connection('192.168.1.7.1.1', 853)
    plc.open()
    print("Opened!")

    # Read a variable
    value = plc.read_by_name('MAIN.myInput', pyads.PLCTYPE_BOOL)
    print(f'Read value: {value}')
    print("READ!")

    # Write a variable
    plc.write_by_name('MAIN.myOutput', True, pyads.PLCTYPE_BOOL)
    print('Wrote value: True')

except pyads.ADSError as e:
    print(f'ADSError: {e}')

finally:
    # Close connection
    plc.close()
    print("Connection closed.")
