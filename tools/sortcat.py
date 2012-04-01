import csv


"""Small self-contained module for sorting the catalog"""

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
	def sortkey(row):
		row = dict(zip(header,row))
		return '|'.join(row[field] for field in ['author', 'title', 'year']).decode('utf-8')
	return sorted(data, key=sortkey)

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
