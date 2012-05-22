import csv
import gdata.spreadsheet.service

def connect():
	gd_client = gdata.spreadsheet.service.SpreadsheetsService()
	gd_client.email = 'david.tolpin@gmail.com'
	gd_client.password = '33banana'
	gd_client.source = 'YungYiddish Catalog Updater'
	gd_client.ProgrammaticLogin()
	return gd_client

def yycatkey(gd_client):
	"""retrieves catalog key"""
	feed = gd_client.GetSpreadsheetsFeed()
	for i, entry in enumerate(feed.entry):
		if entry.title.text=='Yung-Yidish-Book-Catalog':
			key = entry.id.text.split('/')[-1]
			return key

def sheetid(gd_client, skey, sheet):
	"""retrieves worksheet id for the booklist"""
	feed = gd_client.GetWorksheetsFeed(skey)
	for i, entry in enumerate(feed.entry):
		if entry.title.text==sheet:
			wid = entry.id.text.split('/')[-1]
			return wid

def download(gd_client, outp, sheet='booklist'):
	"""writes the book list as a CSV to outp"""
	skey = yycatkey(gd_client)
	wid = sheetid(gd_client, skey, sheet)
	feed = gd_client.GetCellsFeed(skey, wid)
	cat = csv.writer(sys.stdout)
	icol, irow = "A", ""
	lastcol = "A"
	row = []

	for i, entry in enumerate(feed.entry):
		jcol, jrow = entry.title.text[:1], entry.title.text[1:]
		if irow!=jrow:
			if lastcol<icol:
				lastcol = icol
			if row:
				while icol<lastcol:
					row.append("")
					icol = chr(ord(icol)+1)
				cat.writerow(row)
				row = []
			icol, irow = "A", jrow
		while icol!=jcol:
			row.append("")
			icol = chr(ord(icol)+1)
		row.append(entry.content.text)
		icol = chr(ord(icol)+1)
	# flush the last line
	if row:
		while icol<lastcol:
			row.append("")
			icol = chr(ord(icol)+1)
		cat.writerow(row)

if __name__=="__main__":
	import sys
	gd_client = connect()
	download(gd_client, sys.stdout, *sys.argv[1:])


