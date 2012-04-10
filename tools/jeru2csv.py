import sys
import re
import csv

prevline = ""
outp = csv.writer(sys.stdout)
fields = []
skiprecord = False
for line in sys.stdin:
	line = line.strip() \
		.replace("&quot;", "\"") \
		.replace("&amp;", "&") \
		.replace("&aacute;", "a") \
		.replace("&acirc;", "a") \
		.replace("&nbsp;", " ")
	
	
	if prevline:
		line = prevline+" "+line
	if re.search("href", line):
		skiprecord = True
		prevline = ""
	elif re.search("<tr", line):
		prevline = ""
		if not skiprecord and len(fields)>=5 and any(fields):
			outp.writerow(fields)
		fields = []
		skiprecord = False
	elif re.search("<td", line):
		if re.search("</td>", line):
			prevline = ""
			field = (re.search("<td[^>]*>(.*)</td", line) 
					 .group(1).decode('windows-1255')
					 .encode('utf-8')
					 .strip())
			field = re.sub("<span[>]*>", "", field)
			field = re.sub("</span>", "", field)
			colspan = re.search("colspan=([1-9])", line)
			if colspan:
				colspan = int(colspan.group(1))
			else:
				colspan = 1
			for i in range(colspan):
				fields.append(field)

