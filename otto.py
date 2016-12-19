from ola.ClientWrapper import ClientWrapper
from pythonosc import osc_message_builder
from pythonosc import udp_client
import random


def NewData(data):
  #print data
  for x in range(10):
  	address = "/0/chan/%d"%x
  	percents = int (data[x]/255*100)
  	oscoutput.send_message(address, percents)



oscoutput = udp_client.SimpleUDPClient("192.168.1.120", 9000)
universe = 1

wrapper = ClientWrapper()
client = wrapper.Client()
client.RegisterUniverse(universe, client.REGISTER, NewData)
wrapper.Run()