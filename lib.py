#!/usr/bin/python

import socket 
import sys
import os


class VidBlaster:
	def __init__(self,ip='127.0.0.1',port=9998):
		try:
			self.ip = os.environ["VBHOST"]
		except KeyError:
			self.ip = ip
		try:
			self.port = os.environ["VBPORT"]
		except KeyError:
			self.port =port

		print "Connecting to ",self.ip,self.port
		self.sock = socket.create_connection((self.ip,self.port))
		print self.sock.recv(4096)

	def sendCommand(self,cmd):
		#print cmd
		self.sock.send(cmd)
		self.sock.recv(4096)

	def sendTextToOverlay(self,text,overlay):

		self.sendCommand("""apiwrite %s, text, %s\n"""%(overlay,text))

	def turnOverlay(self,onoff,overlay):
		if onoff:
			o="on"
		else:
			o="off"
		self.sendCommand("""apiwrite %s, %s, 1\n"""%(overlay,o))
#vb = VidBlaster()
# These functions exist to keep compatibility with the original scripts
# because I ran out of time.
def sendCommand(cmd):
	vb.sendCommand(cmd)
def turnOverlay(onoff,overlay):
	vb.turnOverlay(onoff,overlay)
def sendTextToOverlay(text,overlay):
	vb.sendTextToOverlay(text,overlay)

if __name__ == "__main__":
	vb.sendTextToOverlay(sys.argv[1],"Video Overlay 1")
