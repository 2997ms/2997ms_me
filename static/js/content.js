$(document).ready(function() {
  $('#pgp-btn').click(function() {
    $('#pgpkey').modal();
    window.location.hash = "#pgp";
  })

  $('#pgp-btn-close').click(function() {
    window.location.hash = "";
  })

  if (window.location.hash == "#pgp") {
    $('#pgpkey').modal();
  }

  $('a').click(function() {
    if (this.href.match('^' + window.location.origin)) {
      var path = this.href.replace(window.location.origin, '');
      ga('send', 'pageview', path);
    } else {
      ga('send', 'event', 'link', 'click', this.href);
    }
  });

  $('.page-scroll a').bind('click', function(e) {
      var $anchor = $(this);
      $('html, body').stop().animate({
          scrollTop: $($anchor.attr('href')).offset().top
      }, 1500, 'easeInOutExpo');
      e.preventDefault();
  });
});
