import argparse,bgblink,time
from lumberjack import log

VERBOSE = False

COMMANDS = {0x00: "PING"}

def gbgc(x,o):
	log("{:02X} {}".format(x,COMMANDS.get(x,"INVALID")),">","cyan")
	if x==0x00:
		log("00 PING","<","cyan")
		return x
	log("FF INVALID","<","red")
	return 0xFF

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
