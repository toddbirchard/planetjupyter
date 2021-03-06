$(document).ready(function() {
  var api_url = 'https://api.linkpreview.net/';
  base_external_url = '/notebook'

  function verifyImage(input) {
    if (input.length > 0) {
      return '<div class="preview-image" style="background-image:url(' + input + ');"></div>'
    } else {
      return "";
    }
  }

  function verifyTitle(input) {
    if (input.title == "") {
      return input.url;
    } else {
      return input.title;
    }
  }

  function postLinkPreviews() {
    $('.sidebar a').each(function(index, element) {
      var target = $(this).attr('href');
      $.ajax({
        url: api_url + "?key=5b439c179073fae7b9928e83dc64e969bd01b9562d693&q=" + $(this).text(),
        contentType: "application/json",
        dataType: 'json',
        success: function(result) {
          var link_image = verifyImage(result.image);
          var verify_title = verifyTitle(result);
          console.log(result);
          $(element).after('<a class="recentnotebook" href="' + target + '"><div class="link-preview"><h4>' + verify_title + '</h4><div class="link-info">' + link_image + '<p>' + result.description + '</p></div></div></a>');
          $(element).remove();
          $(".sidebar a").click(function(event) {
            event.preventDefault();
            target = target.replace("https://github.com/", "https://raw.githubusercontent.com/")
            $('input').val(target);
            $("form").submit();
        });
      }
    });
  });
}


  postLinkPreviews();
});
