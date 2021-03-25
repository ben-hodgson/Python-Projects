import Adafruit_DHT
import time
import datetime
from datetime import date
from openpyxl import load_workbook

# set sensor 
DHT_SENSOR = Adafruit_DHT.DHT11
# set pin 
DHT_PIN = 4

# load spreadsheet
wb = load_workbook('/home/pi/Desktop/weather.xlsx')
sheet = wb['Sheet1']

# create infinite loop to gather temperature
try:
    while True:
        # get temperature and humidity from sensor
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        # get date
        today = date.today()
        # get current time
        now = datetime.datetime.now().time()
        # print date, time and current readings to terminal
        if humidity is not None and temperature is not None:
            print('Adding this data to the spreadcheet:')
            print(today)
            print(now)
            print("{0:0.1f}C {1:0.1f}%".format(temperature, humidity))

            # write new row of readings to spreadsheet
            row = (today, now, temperature, humidity)
            sheet.append(row)
            # save spreadsheet
            wb.save('/home/pi/Desktop/weather.xlsx')
        else:
            # print error if no reading from DHT-11
            print("Sensor failure. Check wiring.");
        # set sleep time for ten minutes
        time.sleep(600);
finally:
    #CTRL+C to save weather.xlsx and quit program
    wb.save('/home/pi/Desktop/weather.xlsx')
    print('Goodbye!')
