#!/usr/bin/python

import socket 
import struct
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

	def sendPNGToOverlay(self,data,overlay):
		sock = socket.create_connection((self.ip,self.port))
		sock.recv(4096)
		sock.send("""apiwrite %s, file, [png]\r\n"""%(overlay))
		sock.recv(4096)
		sock.send(struct.pack('>LL',0,len(data)))
		sock.send(data)
		sock.close()

def genTextPNG(text,font="/usr/share/fonts/type1/gsfonts/c059016l.pfb",fsize=48):
	#put these here so that they are not imported until needed
	from wand.image import Image
	from wand.font import Font
	from wand.color import Color

	# convert -size 1000x180 xc:transparent -fx 0 -channel A -fx 'cos(0.6*pi*(i/w-0.5))-0.0' background.png
	img=Image(filename="background.png")
	fontwhite=Font(path=font,color=Color("white"),size=fsize,antialias=True)
	fontblack=Font(path=font,color=Color("black"),size=fsize,antialias=True)
	img.caption(text,font=fontblack,gravity='center',left=8,top=8)
	img.caption(text,font=fontwhite,gravity='center')
	final = Image(width=1280,height=720)
	final.composite(img,90,510)
	return final


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
