from uljeru import *

def download(gd_client, outp):
	print "Downloading"
	skey = yycatkey(gd_client)
	wid = bklistid(gd_client, skey)
	print "Getting feed ... ",
	feed = gd_client.GetCellsFeed(skey, wid)
	print "got"
	cat = csv.writer(sys.stdout)
	for i, entry in enumerate(feed.entry):
		print entry.content.title
	

if __name__=="__main__":
	import sys
	gd_client = connect()
	download(gd_client, sys.stdout)


