import requests
import pigpio
from time import sleep

pi = pigpio.pi()
gpio_pin = 18

DOMAIN = "yqozl5nyoqxf.kintone.com"
API_TOKEN = "P2gOuITnHxDLPn25OpzozJUO6UboJCQdUlMad67y"
APP_ID = "2"
url = f"https://{DOMAIN}/k/v1/records.json"
headers = {"X-Cybozu-API-Token": API_TOKEN}

def kintone_pel_num():
    global url
    global headers
    params = {
        "app": APP_ID,
        #$id is the record id, orders from newest to olest, gets the most recent one
        
        "query": "order by $id desc limit 1"
        }


    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status() #error signal sends

    records = r.json()["records"] #json into dictionary


    if records:
        return int(records[0]["pellets_num"]["value"])  # field code must match Kintone
    return 0

def dispense_pellets(count):
    for x in range(count):
        pi.set_servo_pulsewidth(gpio_pin, 1500)  # move to dispense position
        sleep(0.5)                           # wait half a second
        pi.set_servo_pulsewidth(gpio_pin, 1000)  # return to rest position
        sleep(0.5)

while True:
    global url
    pellets = kintone_pel_num()
    if pellets > 0:
        print(f"Dispensing {pellets} pellets")
        dispense_pellets(pellets)

        update_data = {
    "app": APP_ID,
    "record": {
        "pellets": {"value": 0}
    }
}
    requests.put(url, headers=headers, json=update_data)

    sleep(5)  # check every 5 seconds
