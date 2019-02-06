(function(){
  var site_url = 'https://bookmarks753.serveo.net/';
  if (window.myBookmarklet !== undefined){
    myBookmarklet();
  } else {
    document.body.appendChild(document.createElement('script')).src=site_url+'static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
  }
})();
