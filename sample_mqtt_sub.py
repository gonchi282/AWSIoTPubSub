from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient as mqttclient
import time
import json

def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")



mymqttclient = mqttclient("clientID", useWebsocket=True)
mymqttclient.configureEndpoint("a1l45l44mj04ay-ats.iot.us-west-2.amazonaws.com", 443)
mymqttclient.configureCredentials("rootCA2.crt")

mymqttclient.configureAutoReconnectBackoffTime(1, 32, 20)
mymqttclient.configureOfflinePublishQueueing(-1)
mymqttclient.configureDrainingFrequency(2)
mymqttclient.configureConnectDisconnectTimeout(10)
mymqttclient.configureMQTTOperationTimeout(5)

mymqttclient.connect()
print("Connect\n")

while True:
	mymqttclient.subscribe("topic/data", 1, customCallback)
	time.sleep(1)

