$(document).ready(function() {
  $('#contact-form').on('submit', function(e){

    //Disable button and disable normal operation
    $('#contact-submit').prop("disabled", true);
    $('#contact-submit').val("Sending...");
    e.preventDefault();

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
      $('#contact-submit').val("Submit");
    }, 2000);

    return false;
  });
});
