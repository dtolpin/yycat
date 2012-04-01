#!/usr/bin/env python
# coding: utf-8

import csv
from sortcat import read, sortkey

"""Small self-contained module for splitting the catalog"""
SECTIONS = [
	[u'א', 'alef'],
	[u'ב', 'beys'],
	[u'ג', 'gimel'],
	[u'ד', 'daled'],
	[u'ה', 'hey'],
	[u'ו', 'vov'],
	[u'ז', 'zayin'],
	[u'ח', 'khes'],
	[u'ט', 'tes'],
	[u'י', 'yud'],
	[u'כ', 'khaf'],
	[u'ל', 'lamed'],
	[u'מ', 'mem'],
	[u'נ', 'nun'],
	[u'ס', 'samekh'],
	[u'ע', 'ayin'],
	[u'פ', 'pey'],
	[u'צ', 'tzadi'],
	[u'ק', 'kuf'],
	[u'ר', 'reysh'],
	[u'ש', 'shin'],
	[u'ת', 'tof'],
    [u'\0', '']]

def split(header, data):
	"split the catalog into separate CSV files for each letter"
	sec = u'\0'
	sections = SECTIONS[:]
	outf = file("/dev/null")
	outw = None
	for row in data:
		key = sortkey(dict(zip(header, row)), '').strip()
		if key[0] != sec:
			outf.close()
			sec, outname = sections.pop(0)
			outf = file(outname+".csv", "w")
			outw = csv.writer(outf)
			outw.writerow(header)
		outw.writerow(row)
	outf.close()

if __name__ == "__main__":
	import sys
	header, data = read(sys.stdin)
	split(header, data)
			
			
		



