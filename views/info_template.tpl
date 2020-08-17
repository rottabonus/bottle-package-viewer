<div>
  <div>
    <h1>{{name}}<h1>
  </div>
  <div>
      <h2>Description</h2>
      <p>{{status['packages'][name]['description']}}</p>
  </div>
  <div>
  <h2>Dependencies</h2>
  <ul>
    %for depend in status['packages'][name]['depends']:
    <li><a href="{{depend}}" > {{depend}} </a></li>
    %end
</ul>
  </div>
  %if name in status['reverse_depends_dict'].keys():
      <div>
        <h2>Reverse-depends</h2>
          <ul>
        %for item in status['reverse_depends_dict'][name]:
            <li><a href="{{item}}"> {{item}}</a></li>
        %end
          </ul>
      </div>
    %end
  </div>
</div>
