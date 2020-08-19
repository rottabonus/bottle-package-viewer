
<!doctype html>
<html lang="fi">
  <head>
    <meta charset="utf-8">
    <title>bottle-pkg-viewer</title>
    <link rel="stylesheet" href="/static/style.css">
    <link rel="icon" type="image/png" href="/static/favicon.ico"/>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  </head>
<body>

<div class="package-container">

  <div class="name-div">
    <div class="package-name">
      <h1>{{name}}<h1>
    </div>
    <div class="back-icon">
      <a href="/"><i class="fa fa-arrow-circle-o-left" style="font-size:36px"></i></a>
  </div>
</div>

  <div class="description-div">
      <h2>Description</h2>
      <p>
      %for line in status['packages'][name]['description']:
          %if line.strip() == '.':
            <br>
          %else:
          {{line}} <br>
          %end
      %end
      </p>
  </div>

  <div class="dep-div">
    <div>
    %if len(status['packages'][name]['depends']) != 0:
    
    <h2>Dependencies</h2>
    <ul>
      %for depend in status['packages'][name]['depends']:
          %if depend in status['packages'].keys():
        
              <li><a href="/packages/{{depend}}" > {{depend}} </a></li>
      
          %else: 
              <li>{{depend}}</li>
      
          %end
      %end
    </ul>
   %end
 
    </div>
    %if name in status['reverse_depends_dict'].keys():
        
        <div>
          <h2>Reverse-depends</h2>
            <ul>
          %for item in status['reverse_depends_dict'][name]:
              
              <li><a href="/packages/{{item}}"> {{item}}</a></li>
          %end
            </ul>
        </div>
      %end
    </div>
  </div>

</div>
</body>
</html>
