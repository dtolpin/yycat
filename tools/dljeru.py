from uljeru import *

def download(gd_client, outp):
	print "Downloading"
	skey = yycatkey(gd_client)
	wid = bklistid(gd_client, skey)
	print "Getting feed ... ",
	feed = gd_client.GetCellsFeed(skey, wid)
	print "got"
	cat = csv.writer(sys.stdout)
	irow = ""
	row = []
	for i, entry in enumerate(feed.entry):
		jrow = entry.title.text[1:]
		if irow!=jrow:
			if row:
				cat.writerow(row)
				row = []
			irow = jrow
		row.append(entry.content.text)

if __name__=="__main__":
	import sys
	gd_client = connect()
	download(gd_client, sys.stdout)


