#!/usr/bin/env python

import sys
import qrcode
from qrcode.image.svg import SvgFragmentImage
import csv

MAX_FIELD_LENGTH = 12

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
        width: 2.25in; height: 2.5in;
        padding: 0;
        float: left;
        border: thin solid gray;
	    page-break-inside: avoid;
        text-align: center;
        font-family: sans serif;
      }
      div.qrcode p {padding: 0; margin: 0;}
    </style>
  </head>
  <body>
"""

EPILOGUE="""\
    </body>
  </html>
"""

def mksheet():
	print PROLOGUE
	cat = csv.reader(sys.stdin)
	
	cat.next() # skip the header
	for row in cat:
		call_number = row[0]
		count = int(row[1])
		del row[1]
		info = "\n".join(word.decode('utf-8').strip()[:MAX_FIELD_LENGTH].encode('utf-8')
						 for word in row if word)
		
		for i in range(count):
			print "    <div class=\"qrcode\">"
			print "      <p>%s</p>" % call_number
			mklbl(info)
			print "    </div>"
		
	print EPILOGUE


if __name__ == "__main__":
	mksheet()
