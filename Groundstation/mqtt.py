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
    C = "3751,15:28:44,227,C,F,R,N,2.93,30.03,3.46,00:00:00,0.000000,0.000000,0.00,0,RELEASED_1,0,0,CXON"
    S1 = "3751,00:00:00,176,SP1,10.57,28.57,0.60,0.000000,0.000000,9.77,1.41,0.52"
    S2 = "3751,00:00:00,783,SP2,0.89,35.57,240.52,0.000000,0.000000,9.66,0.39,-0.57"
    while True:
        time.sleep(0.1)
        mqttc.publish('teams/3751', C)  # send the line of data
        print(C)
        time.sleep(0.1)
        mqttc.publish('teams/3751', S1)  # send the line of data
        print(S1)
        time.sleep(0.1)
        mqttc.publish('teams/3751', S2)  # send the line of data
        print(S2)
        time.sleep(0.7)
        print("pingsen")



if __name__ == "__main__":
    mqttc = Initialise_client()
    test()
