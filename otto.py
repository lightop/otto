#!/usr/bin/python3

from ola.ClientWrapper import ClientWrapper
from pythonosc import osc_message_builder
from pythonosc import udp_client
import cmd
import socket

class OttoShell(cmd.Cmd):

	def do_run (self, arg):
		oscoutput = udp_client.SimpleUDPClient(ip_address, port)
		universe = 1
		wrapper = ClientWrapper()
		client = wrapper.Client()
		client.RegisterUniverse(universe, client.REGISTER, NewData)
		wrapper.Run()

	def do_ip (self, arg):
		print (arg)
		try:
			socket.inet_aton(arg)
			ip_address = arg
			print (ip_address)
		except socket.error:
			print ("Not an address")

	def do_port (self,arg):
		try:
			arg = int(arg)
		except ValueError:
			print("Ой!")

	def do_status(self,arg):
		print (ip_address)
		print (port)

	def do_exit(self,arg):
		print ("До свидания!")
		return True




		
ip_address = "192.168.1.124"
port = 9000


def NewData(data):
  value = 0
  for x in range(10):
  	address = "/0/chan/%d"%x
  	percents = int (data[x]/255*100)
  	if percents == 0:
  		value = "-"
  	
  	elif percents >=100:
  		value = "FL"
  	
  	else:
  		value = percents
  	
  	oscoutput.send_message(address, value)


cmd = OttoShell()
cmd.prompt = '>'
cmd.intro = "Welcome to OTTO"


cmd.cmdloop()