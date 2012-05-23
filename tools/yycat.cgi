#!/bin/sh

# configuration variables

HOME=${HOME:-/home/dvd}
PATH=$HOME/bin:$PATH
HTMLDIR=$HOME/public_html/yycat/html
TOOLDIR=$HOME/work/yycat/tools
HTMLURL=/~dvd/yycat/html

# end of configuration

if echo $QUERY_STRING|grep -q generate ; then
   (cd $HTMLDIR; $TOOLDIR/cat2html)
fi

cat <<__END_OF_PAGE__
Content-Type: text/html

<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Yung Yiddish Catalog HTML export</title>
    <style type="text/css">
      h1 {font-size: 144%}
      input[type=submit] {font-size: 120%; font-weight: bold}
      body {direction: rtl; font-family: sans-serif}
    </style>
  </head>
  <body>
    <h1>יונג יידיש: אַ רשימה פון די ביכער אױף HTML</h1>
    <div style="float: right">
      <form action="" method="get">
        <p>
          <input type="submit" name="generate" value="שאַפן" />
        </p>
      </form>
    </div>
    <div style="float: right">
      <ul>
        <li><a href="$HTMLURL/jeru/alef.htm" target="yycat:jeru">ירושלמער זאַמלונג</a></li>
        <li><a href="$HTMLURL/tlv/alef.htm" target="yycat:tlv">תל־אביבער זאַמלונג</a></li>
        <li><a href="$HTMLURL/jeru,tlv/alef.htm" target="yycat:jeru,tlv">אַלגעמײַנע זאַמלונג</a></li>
      </ul>
    </div>
    <div style="clear: both">
      <h2>עטיקעטן</h2>
      <ul>
        <li><a href="yycat-mklbl?jeru">ירושלם</a></li>
        <li><a href="yycat-mklbl?ta">תל אביב</a></li>
      </ul>
    </div> 
  </body>
</html>
__END_OF_PAGE__
