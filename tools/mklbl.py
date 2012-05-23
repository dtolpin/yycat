#!/usr/bin/env python

import sys
import qrcode
from qrcode.image.svg import SvgFragmentImage
import csv

MAX_FIELD_LENGTH = 14
NCOLS = 3
NROWS = 3

def mklbl(info):
	"""print qrcode to stdout"""
	qr = qrcode.QRCode()
	qr.add_data(info)
	img = qr.make_image(image_factory=SvgFragmentImage)
	img.save(sys.stdout)

PROLOGUE="""\
<?xml version="1.0" encoding="utf-8"?>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style type="text/css">
      body { margin: 0; padding: 0}
      div.qrcode {
        width: 2.4in; height: 2.6in;
        padding: 0;
        float: left;
        border: thin solid gray;
	    page-break-inside: avoid;
        text-align: center;
        display-align: center;
        font-family: sans serif;
      }
      table { border-collapse: collapse; }
      td { padding: 0; vertical-align: middle; }
      div.qrcode p {padding-top: 6pt; margin: 0; font-family: sans serif }
    </style>
  </head>
  <body>
"""

EPILOGUE="""\
    </body>
  </html>
"""

def squeezed(row):
	"""squeeze the info if two long"""
	row = [word.strip() for word in row if not word.isspace()]
	if sum(len(word) for word in row) > MAX_FIELD_LENGTH*len(row):
		# squeeze only if the *total length* is too large
		row = [word.decode('utf-8')[:MAX_FIELD_LENGTH].encode('utf-8') for word in row]
	return row

def mksheet():
	print PROLOGUE
	cat = csv.reader(sys.stdin)
	
	cat.next() # skip the header
	print "<table><tr>"
	icell = 0
	irow = 0
	for row in cat:
		call_number = row[0]
		count = int(row[1])
		del row[1]
		info = "\n".join(squeezed(row))
		
		for i in range(count):

			if icell==NCOLS:
				icell = 0
				print "</tr>"
				irow+=1
				if irow==NROWS:
					irow = 0
					print "<tr style=\"page-break-before: always\">"
				else:
					print "<tr>"

			print "    <td>"
			print "      <div class=\"qrcode\">"
			print "        <p>%s</p>" % call_number
			mklbl(info)
			print "      </div>"
			print "    </td>"
			icell+= 1
	print "</tr></table>"
		
	print EPILOGUE


if __name__ == "__main__":
	mksheet()
