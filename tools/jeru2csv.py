import sys
import re
import csv

prevline = ""
outp = csv.writer(sys.stdout)
fields = []
for line in sys.stdin:
	if prevline:
		line = prevline + line
	if re.search("<tr", line):
		if fields:
			outp.writerow(fields)
			fields = []
	elif re.search("<td.*class=xl28", line):
		if re.search("</td>", line):
			prevline = ""
			fields.append(re.search(">([^<]*)", line)
						  .group(1).decode('windows-1255').encode('utf-8').strip())

