function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function() {
  $('#contact-form').on('submit', function(e){

    //Disable button and disable normal operation
    $('#contact-submit').prop("disabled", true);
    $('#contact-submit').val("Sending...");
    e.preventDefault();


    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    //Send the form
    $.ajax({
      data: $(this).serialize(),
      type: $(this).attr('method'),
      url: $(this).attr('action'),
      success: function(response) {
        setTimeout(function() {
          $('#contact-output').text(response);
        }, 750);
      },
    });

    //Re-enable button after some time
    setTimeout(function() {
      $('#contact-form').find("input, textarea").val("");
      $('#contact-submit').prop("disabled", false);
      $('#contact-submit').val("Sent!");
    }, 750);

    //Return to 'Submit' text
    setTimeout(function() {
      $('#contact-submit').val("Send");
      $('#contact-output').text("");
    }, 2000);

    return false;
  });
});
