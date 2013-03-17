#!/usr/bin/python

import socket 
import sys

port=9998
ip="192.168.1.4"
ip="10.146.143.33"



class VidBlaster:
	def __init__(self,ip='127.0.0.1',port=9998):
		self.ip = ip
		self.port =port

		self.sock = socket.create_connection((ip,port))
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

vb = VidBlaster(ip,port)

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
