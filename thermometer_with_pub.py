from PiAnalog import *
import pub
import time
from gpiozero import LED
import json

CONFIG_FILE = "key-temperature-pub-sub-account.json"
with open(CONFIG_FILE) as config_file:
    config = json.load(config_file)


red_led = LED(24)
red_led.on()
p = PiAnalog()


# Update the temperature reading
def update_temp():
    temperature = p.read_temp_c()
    temperature = "%.2f" % temperature # Round the temperature to 2 d.p. 
    print (f"new temperature is: {temperature} - sending this to pub topic")

    pub.publish(temperature, config["project_id"], config["topic_id"])


while True:
    update_temp()
    time.sleep(30)
