import argparse,bgblink,time

test = lambda x: x

try:
	link = bgblink.BGBLinkCable("127.0.0.1",8765)
	link.setExchangeHandler(test)
	link.start()
	while True:
		time.sleep(10)
except:
	pass
