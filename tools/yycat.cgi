#!/bin/sh

if echo $QUERY_STRING|grep -q generate ; then
   (cd ~/public_html/yycat/html; ../tools/cat2html)
fi

cat <<__END_OF_PAGE__
Content-Type: text/html

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
        <li><a href="/~dvd/yycat/html/jeru/alef.htm" target="yycat:jeru">ירושלמער פֿערזאַמלונג</a></li>
        <li><a href="/~dvd/yycat/html/tlv/alef.htm" target="yycat:tlv">תל־אביבער פֿערזאַמלונג</a></li>
        <li><a href="/~dvd/yycat/html/jeru,tlv/" target="yycat:jeru,tlv">אַלגעמײַנע פֿערזאַמלונג</a></li>
      </ul>
    </div>
  </body>
</html>
__END_OF_PAGE__     