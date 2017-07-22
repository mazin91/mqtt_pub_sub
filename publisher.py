import paho.mqtt.client as mqtt
import time
import json
import random

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("user") 

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(client_id="rashid")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
while client.loop() == 0:
    #0-1000 Deira Dubai
    #1000-1050 Abu Shagara
    #1050-1150 University City
    user=random.randrange(1050, 1150)
    val={"user":user,"house_id":user+3,"device_id":user*51,"city":"University City","state":"Sharjah","current":random.randrange(20, 28),"temperature":random.randrange(20, 28),"humidity":random.randrange(40, 58),"time":int(round(time.time() * 1000))}
    val=json.dumps(val)
    print val
    client.publish("Sensor",str(val) ,0,False)
    time.sleep(1)# sleep for 1 second before next call
