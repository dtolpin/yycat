#!/bin/sh

# configuration variables

HOME=${HOME:-/home/dvd}
PATH=$HOME/bin:$PATH
TOOLDIR=$HOME/work/yycat/tools

echo Content-Type: text/html
echo 
$TOOLDIR/cat2lbl $QUERY_STRING
