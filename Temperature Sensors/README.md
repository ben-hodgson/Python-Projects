# Temperature Sensors

## DHT11.py

This program will read the temperature and humidity from a DHT11 sensor. It will output the readings to the terminal and also store them in a xlsx file.

## BMP280.py

This program is nearly the same as **DHT11.py**, it will read the temperature, pressure, and humidity from a [Pimoroni BMP280](https://shop.pimoroni.com/products/bmp280-breakout-temperature-pressure-altitude-sensor) sensor. It will output the readings to the terminal and also store them in a xlsx file.

## air-mon.py

This is a program that I have created to work with the [Air monitor hat](https://shop.sb-components.co.uk/products/air-monitoring-hat-for-raspberry-pi) from SB Components. The hat contains a PMSA003 sensor to monitor partical matter at 1, 2.5, and 10 micrometers (μm). Included is the python libary for the sensor. There is also a BME280 sensor attached to the GPIO extention pins on the hat to gather temperature, humidity, and pressure readings aswell, the libary for this sensor will have top be installed using pip. The readings are then converted into json and are then sent to a Node_Red instance using the **paho mqtt** libary that can be installed using pip.
There is also another shell script that I have created to run the **air-mon.py** program as every so often the PMSA003 sensor would fail to get a reading and stop the python program. The shell script will restart the python file when an error occurs.