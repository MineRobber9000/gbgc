import argparse,bgblink,time
from lumberjack import log as log_important

VERBOSE = False

def log(*args):
	if not VERBOSE:
		return
	log_important(*args)

STANDBY, RECV_NAME, SEND_DATA = range(3)

STATE = STANDBY

NAME = ""
DATA = []

def getData(loc):
	global DATA
	DATA = [ord(x) for x in loc]

COMMANDS = {0x00: "PING",0x01:"RETR"}

def gbgc(x,o):
	global STATE, NAME, DATA
	if STATE==STANDBY:
		log("{:02X} {}".format(x,COMMANDS.get(x,"INVALID")),">","cyan")
		if x==0x00:
			log("00 PING","<","cyan")
			return x
		elif x==0x01:
			log("01 ACK, state switch to RECV_NAME","<","green")
			STATE = RECV_NAME
			NAME = ""
			return 0x01
		log("FF INVALID","<","red")
		return 0xFF
	elif STATE==RECV_NAME:
		log("{:02X} {!s}".format(x,(chr(x) if x!=0x00 else "<END>")),">","cyan")
		if x==0x00:
			log("02 ACK_FIN, state switch to SEND_DATA","<","green")
			STATE = SEND_DATA
			getData(NAME)
			return 0x02
		NAME += chr(x)
		log("01 ACK","<","yellow")
		return 0x01
	elif STATE==SEND_DATA:
		if len(DATA)==0:
			log("FF END_PACKET, state switch to STANDBY","<","green")
			STATE=STANDBY
			return 0xFF
		r = DATA.pop(0)
#		log("{:02X}".format(x),">","cyan")
		log("{:02X}".format(r),"<","green")
		return r

if __name__=="__main__":
	try:
		parser = argparse.ArgumentParser(description="Connects BGB to the GBGC protocol and server.",epilog="Host and port default to 127.0.0.1:8765.")
		parser.add_argument("host",default="127.0.0.1",nargs="?",help="Host to connect to.")
		parser.add_argument("port",default=8765,type=int,nargs="?",help="Port to connect to.")
		args = parser.parse_args()
		log("Connecting to host \"{}\" and port {!s}".format(args.host,args.port))
		link = bgblink.BGBLinkCable(args.host,args.port)
		link.setExchangeHandler(gbgc)
		log("Connecting...")
		link.start()
		log("Connected!","*","green")
		while True:
			time.sleep(10)
	except Exception as e:
		log("An error occurred: \"{}: {!s}\"".format(e.__class__.__name__,e),"X")
		pass
