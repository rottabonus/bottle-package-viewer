<div>
  <div><h2>Packages:<h2></div>
    <div>
      <ul>
        %for key in status['packages']:
        <li><a href="/{{key}}"> {{key}} </a></li>
        %end
    </ul>
  </div>
</div>
