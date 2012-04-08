#!/usr/bin/env python
# coding: utf-8

import csv

"""Small self-contained module for sorting the catalog"""

def sortkey(rowdict):
	"""return the sort key of the row dictionary"""
	key = ''.join(rowdict[field] for field in ['author', 'title', 'year']).decode('utf-8')
	if key[0] < u'א':
		key = u'א'+key # everything before alef goes to alef
	return key

def read(inp):
	"""read the catalog, return header and data"""
	cat = csv.reader(inp)
	
	header = cat.next()
	data = []
	for row in cat:
		data.append(row)
		
	return header, data
	
def sort(header, data):
	"""Sorts the catalog data alphabetically by author, then title, then year"""
	return sorted(data, key=lambda row: sortkey(dict(zip(header, row))))

def write(outp, header, data):	
	"""write catalog to CSV file"""
	cat = csv.writer(outp)
	cat.writerow(header)
	cat.writerows(data)

def sortcat(inp, outp):
	"""sort CSV catalog"""
	header, data = read(sys.stdin)
	data = sort(header, data)
	write(sys.stdout, header, data)

if __name__ == "__main__":
	import sys
	sortcat(sys.stdin, sys.stdout)
