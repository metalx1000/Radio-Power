#!/bin/bash
echo -en "Content-Type: text/html\r\n\r\n"

cat << EOH
<!DOCTYPE html>
<html lang="en">
<head>
  <title></title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/bootstrap.min.css">
  <script src="/jquery.min.js"></script>
  <script src="/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <h2>FILES</h2>
  <div id="list" class="list-group">
EOH

#create list
#ls -a --group-directories-first ..${REQUEST_URI#${SCRIPT_NAME}}|while read line
ls -a "..${REQUEST_URI#${SCRIPT_NAME}}"|while read line
do
  echo "<a href='$line' class='list-group-item'>$line</a>"
done

cat << EOF
  </div>
</div>

</body>
</html>
EOF
