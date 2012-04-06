import csv
import gdata.spreadsheet.service

def connect():
	gd_client = gdata.spreadsheet.service.SpreadsheetsService()
	gd_client.email = 'yybkcat@gmail.com'
	gd_client.password = '5i5ernoter'
	gd_client.source = 'YungYiddish Catalog Updater'
	gd_client.ProgrammaticLogin()
	return gd_client

def yycatkey(gd_client):
	feed = gd_client.GetSpreadsheetsFeed()
	for i, entry in enumerate(feed.entry):
		if entry.title.text=='Yung-Yidish-Book-Catalog':
			key = entry.id.text.split('/')[-1]
			return key

def bklistid(gd_client, skey):
	feed = gd_client.GetWorksheetsFeed(skey)
	for i, entry in enumerate(feed.entry):
		if entry.title.text=='booklist':
			wid = entry.id.text.split('/')[-1]
			return wid

def download(gd_client, outp):
	skey = yycatkey(gd_client)
	wid = bklistid(gd_client, skey)
	feed = gd_client.GetCellsFeed(skey, wid)
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
	print >>sys.stderr, "Downloading ...",
	download(gd_client, sys.stdout)
	print >>sys.stderr, "done"

