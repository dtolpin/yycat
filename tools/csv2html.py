#!/usr/bin/env python
# coding: utf-8

import csv
import sys, getopt

def row2html(row):
	return """\
      <tr>
        <td class="author">%(author)s</td>
        <td class="title">%(title)s</td>
        <td class="city">%(city)s</td>
        <td class="country">%(country)s</td>
        <td class="publisher">%(publisher)s</td>
        <td class="year">%(year)s</td>
      </tr>
""" % row

HEADER="""\
<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Yung Yiddish Catalog (%s)</title> <!-- Combined, Tel Aviv, or Jerusalem -->
    <link rel="stylesheet" type="text/css" href="yycat.css" />
  </head>
  <body>
    <h1>יונג ײדיש%s: א רשימה פון די ביכער</h1>
    <div class="index">
      <a href="alef.htm">א</a>
      <a href="beys.htm">ב</a>
      <a href="gimel.htm">ג</a>
      <a href="daled.htm">ד</a>
      <a href="hey.htm">ה</a>
      <a href="vov.htm">וו</a>
      <a href="zayin.htm">ז</a>
      <a href="khes.htm">ח</a>
      <a href="tes.htm">ט</a>
      <a href="yud.htm">י</a>
      <a href="khaf.htm">כ</a>
      <a href="lamed.htm">ל</a>
      <a href="mem.htm">מ</a>
      <a href="nun.htm">נ</a>
      <a href="samekh.htm">ס</a>
      <a href="ayin.htm">ע</a>
      <a href="pey.htm">פ</a>
      <a href="tzadi.htm">צ</a>
      <a href="kuf.htm">ק</a>
      <a href="reysh.htm">ר</a>
      <a href="shin.htm">ש</a>
      <a href="tof.htm">ת</a>
    </div>
    <table class="booklist">
"""

FOOTER="""\
    </table>
  </body>
</html> 
"""

collection = ['jeru', 'tlv']

optlist, args = getopt.getopt(sys.argv[1:], "c:")

for o, a in optlist:
	if o=="-c":
		collection = a.split(',')

assert len(args) <= 1 # filter or single file

input = sys.stdin
output = sys.stdout
if len(args)==1:
	input = file(args[0], "r")
	assert args[0].find(".csv")!=-1 # protect me from my own bugs
	output = file(args[0].replace(".csv", ".htm"), "w")

inr = csv.reader(input)

tcoll = "combined"
hcoll = ""
if 'jeru' not in collection:
	tcoll, hcoll = "Tel Aviv", " תל אביב"
elif 'tlv' not in collection:
	tcoll, hcoll = "Jerusalem", " ירושלים"
print >>output, HEADER % (tcoll, hcoll)
header = inr.next()
for row in inr:
	row = dict(zip(header, row+['']))
	if (row['jerusalem']>'0') and ('jeru' in collection) or \
	   (row['telaviv']>'0') and ('tlv' in collection):
		print >>output, row2html(row)
output.close()



