#import all the necessary libraries
from machine import ADC,Pin, UART
import utime

#initialize the ADC pin
adc = ADC(Pin(26))

#initialize UART module for bluetooth communication
uart = UART(0, baudrate=9600,tx=Pin(0), rx=Pin(1))

#Reference Voltage and ADC resolution
vref = 3.3 #The maximum voltage the Rapberry PI Pico W can take

adc_resolution = 65535 #The range of values the ADC can output


#Function to convert raw values to voltage

def read_wind_speed():
    adc_value = adc.read_u16()
    voltage = adc_value * vref / adc_resolution
    return voltage

#Function to add or append all incoming data to a data_file

def wind_speed_data_to_file(timestamp_str, voltage):
    try:
        with open("wind_speed_data_file.csv", "a") as data file: #Open data file in an append mode
            data_file.write("{}, {:2f}\n".format(timestamp_str, voltage))
    except Exceptionas e:
        print("Error writing to file:", e)
        
        
#Function to loop the program forever
    
def main():
    while True:
        voltage = read_wind_speed()
        
        # Get the current timestamp
        timestamp = utime.localtime()
        
        # Define the format for the timestamp
        timestamp_str = "{:02d}-{:02d}-{:04d} {:02d}:{02d}:{02d}".format(timestmap[0],timestamp[1],timestamp[2],
                                                                         timestamp[3],timestamp[4],timestamp[5] )
        
        # Append or add wind speed data to file
        wind_speed_data_to_file(timestamp_str, voltage)
        
        #Print the timestamp and voltage to the thonny console or shell
        print("timestamp:{}, Wind Speed in Voltage(V): {:.2f}V", format(timestamp_str, voltage))
        
        #Send the voltage through bluetooth to the App
        uart.write(f"{timestamp_str),{Voltage)\n")
        
        utime.sleep(1)
        
        
        
# initialize the data file with headers if it doesn't exist
try:
    with open("wind_speed_data_file.csv", "r") as data_file:
        pass
except OSError:
    with open("wind_speed_data_file.csv", "w") as data_file:
        data_file.write("Timestamp_str, Voltage\n")
        
        
try:
    main()
except KeyboardInterrupt:
    print("Program Interrupted.")
    