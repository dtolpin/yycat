import sys
import csv
import gdata.spreadsheet.service

def connect():
	gd_client = gdata.spreadsheet.service.SpreadsheetsService()
	gd_client.email = 'david.tolpin@gmail.com'
	gd_client.password = '33banana'
	gd_client.source = 'YungYiddish Catalog Updater'
	gd_client.ProgrammaticLogin()
	return gd_client

COLNAMES = ['year', 'publisher', 'city', 'title', 'author']

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

def upload(gd_client):
	inp = csv.reader(sys.stdin)
	skey = yycatkey(gd_client)
	wid = bklistid(gd_client, skey)
	for row in inp:
		fields = dict(zip(COLNAMES, row))
		fields['jerusalem'] = '1'
		entry = gd_client.InsertRow(fields, skey, wid)

if __name__=="__main__":
	gd_client = connect()
	upload(gd_client)
