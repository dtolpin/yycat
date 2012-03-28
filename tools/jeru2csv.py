import sys
import re
import csv
import HTMLParser
unescape = HTMLParser.HTMLParser().unescape

prevline = ""
outp = csv.writer(sys.stdout)
fields = []
for line in sys.stdin:
	line = line.strip() \
		.replace("&quot;", "\"") \
		.replace("&amp;", "&") \
		.replace("&aacute;", "a") \
		.replace("&acirc;", "a")
	
	
	if prevline:
		line = prevline+" "+line
	if re.search("<tr", line):
		if fields:
			if len(fields)==5 and any(fields):
				outp.writerow(fields)
			fields = []
	elif re.search("<td", line):
		if re.search("</td>", line):
			prevline = ""
			fields.append(re.search(">([^<]*)", line)
						  .group(1).decode('windows-1255').encode('utf-8').strip())

