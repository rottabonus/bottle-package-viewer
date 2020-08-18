<!doctype html>
<html lang="fi">
  <head>
    <meta charset="utf-8">
    <title>bottle-pkg-viewer</title>
    <link rel="icon" type="image/png" href="/static/favicon.ico"/>
    <link rel="stylesheet" href="/static/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
  </head>
<body>
<div>
  <div><h2>Packages:<h2></div>
    <div>
      <ul>
        %for key in status['packages']:
        <li><a href="packages/{{key}}"> {{key}} </a></li>
        %end
    </ul>
  </div>
</div>
</body>
</html>