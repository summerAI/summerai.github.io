var sent = false;
$("#leadform").on("submit", function(event) {
  event.preventDefault();
  var error = false;
  if (!$("input.name").val()) {
    $("input.name").addClass("error");
    error = true;
  }
  if (!$("input.email").val()) {
    $("input.email").addClass("error");
    error = true;
  }
  if (error || sent) {
    return false;
  }
  else {
    sent = true;
    $.ajax({
      type: "POST",
      url: "https://mandrillapp.com/api/1.0/messages/send.json",
      data: {
        'key': '2Imee1LJdN2bT1CZ-7OvyQ',
        'message': {
          'from_email': 'inbound@summer.ai',
          'to': [
            {
              'email': 'hello@summer.ai',
              'name': 'summer.ai',
              'type': 'to'
            }
          ],
          'subject': 'Let\'s Talk about Data',
          'html': 'New lead: ' + $("input.name").val() + "<br>Company: " + $("input.company").val() + "<br>Email or Phone: " + $("input.email").val()
        },
        success: function () {
          $("#leadform .inner").replaceWith("<p class='ok'>Thanks - we'll be in touch in the next 24 hours.</p>");
        },
        error: function () {
          $("#leadform .inner").replaceWith("<p class='ok error'>Oops - something went wrong. Please get in touch with us directly.</p>");
        }
      }
    });
  }

  return false;
});
