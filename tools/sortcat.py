import csv
import sys

### Sorts the CSV catalog file alphabetically:
###  * by author
###  * if there is no author, by title

## read
cat = csv.reader(sys.stdin)

header = cat.next()
data = []
for row in cat:
	data.append(row)

## sort
def sortkey(row):
	row = dict(zip(header,row))
	return (row['author'] or row['title']).decode('utf-8')

data = sorted(data, key=sortkey)

## write
cat = csv.writer(sys.stdout)

cat.writerow(header)
cat.writerows(data)
