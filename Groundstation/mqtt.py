import time

import paho.mqtt.client as mqtt


# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))


def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(client, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(client, obj, level, string):
    print(string)


def Initialise_client():
    mqttc = mqtt.Client()
    # Assign event callbacks
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    # Uncomment to enable debug messages
    topic = 'teams/3751'  # team number
    # Connect
    mqttc.username_pw_set("3751", "Liumgyme567%")  # made up username and password for mqtt
    # establish connection
    mqttc.connect("cansat.info", 1883)
    mqttc.on_log = on_log
    mqttc.loop_start()
    print("init")
    return mqttc


def sendserver(mqttc, Data):
    format = ''
    if len(Data) != 0:
        for i in range(len(Data)):
            format += Data[i] + ','
        # time.sleep(1)  # insert 1 second interval unless payload adata
        mqttc.publish('teams/3751', format)  # send the line of data
    else:
        pass


def test():
    dat = '1111,12:00:00,1,C,F,N,N,1,2,3,12:00:00,4,5,6,7,PRELAUNCH,8,9,10,11,12,13,14,15,16'
    dat2 = '1,2,3,C,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,11,22,33,S1,44,55,66,00,000,000,S2,0000,00000,000000'
    with open('Flight/Flight_3571_C-28.csv') as f:
        Data = f.readlines()
    while True:
        for i in range(len(Data)):
            time.sleep(1)
            mqttc.publish('teams/3751', Data[i])  # send the line of data
            print(Data[i])


if __name__ == "__main__":
    mqttc = Initialise_client()
    test()
