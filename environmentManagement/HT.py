import Adafruit_DHT
from gpiozero import LED
from time import sleep

SENSOR_TYPE = Adafruit_DHT.DHT11
SENSOR_PIN_NUMBER = 4
HEATER_PIN_NUMBER = 2
FAN_PIN_NUMBER = 3
heater = LED(HEATER_PIN_NUMBER)
fan = LED(FAN_PIN_NUMBER)

# relay activates on low signal
def turnOnHeater():
    print("turning heater On")
    heater.off()

def turnOffHeater():
    print("turning heater off")
    heater.on()

def turnOnFan():
    print("turning fan On")
    fan.off()

def turnOffFan():
    print("turning fan Off")
    fan.on()


def getHumidity():
    humidity, temperature = Adafruit_DHT.read_retry(
    SENSOR_TYPE, 
    SENSOR_PIN_NUMBER
    )
    return humidity

def modifyHumidity():
    pass

def getTemp():
    humidity, temperature = Adafruit_DHT.read_retry(
        SENSOR_TYPE, 
        SENSOR_PIN_NUMBER
    )
    return temperature
            
def tempUp():
    turnOnFan()
    sleep(10)
    turnOffFan()
    sleep(10)
    