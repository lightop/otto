#!/usr/bin/python3

from ola.ClientWrapper import ClientWrapper
from pythonosc import osc_message_builder
from pythonosc import udp_client
import cmd
import socket

class OttoShell(cmd.Cmd):

	# def __init__(self):
	# 	self.universe = 1
	# 	self.ip_address = "192.168.2.100"
	# 	self.port = 9000





	def do_run (self, arg):

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
		  	
		  	self.oscoutput.send_message(address, value)

		self.oscoutput = udp_client.SimpleUDPClient(self.ip_address, self.port)
		self.universe =1
		self.wrapper = ClientWrapper()
		self.client = self.wrapper.Client()
		self.client.RegisterUniverse(self.universe, self.client.REGISTER, NewData)
		print ("xscfsdfvcs")
		self.wrapper.Run()
		print("csdvdvdsvcsdvcsdcvsdcccccccc")

	def do_ip (self, arg):
		print (arg)
		try:
			socket.inet_aton(arg)
			self.ip_address = arg
			print (self.ip_address)
		except socket.error:
			print ("Not an address")

	def do_port (self,arg):
		try:
			arg = int(arg)
			self.port = arg
		except ValueError:
			print("Ой!")

	def do_status(self,arg):
		print (self.ip_address)
		print (self.port)

	def do_exit(self,arg):
		print ("До свидания!")
		return True



cmd = OttoShell()
cmd.prompt = '>'
cmd.intro = "Welcome to OTTO"


cmd.cmdloop()