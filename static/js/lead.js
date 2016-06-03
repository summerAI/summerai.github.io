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
        url: "https://formspree.io/you@email.com", 
        method: "POST",
        data: {
          name: $("input.name").val(),
          company: $("input.company").val(),
          email: $("input.email").val()
        },
        dataType: "json",
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
