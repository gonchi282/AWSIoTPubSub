# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
import sys
import random
import datetime

# For certificate based connection
#myMQTTClient = AWSIoTMQTTClient("a1l45l44mj04ay-ats.iot.us-west-2.amazonaws.com")
# For Websocket connection
myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
#myMQTTClient.configureEndpoint("a1l45l44mj04ay-ats.iot.us-west-2.amazonaws.com", 8883)
# For Websocket
myMQTTClient.configureEndpoint("a1l45l44mj04ay-ats.iot.us-west-2.amazonaws.com", 443)
#myMQTTClient.configureCredentials("rootCA2.crt", "22e79ceac2-private.pem.key", "22e79ceac2-certificate.pem.crt")
# For Websocket, we only need to configure the root CA
myMQTTClient.configureCredentials("rootCA2.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()

# Publish message
while True:
	# status
	power = random.randint(0, 1)

	if(power == 0):
		message = '{"power": "off"}' # Power off
	else:
		message = '{"power": "on"}'  # Power on

	myMQTTClient.publish("topic/data", message, 0)
	print(message)
	sleep(1)

myMQTTClient.disconnect()
