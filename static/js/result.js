
$(function () {

  $(".progress").each(function () {

    var value = $(this).attr('data-value');
    var left = $(this).find('.progress-left .progress-bar');
    var right = $(this).find('.progress-right .progress-bar');

    if (value > 0) {
      if (value <= 50) {
        right.css('transform', 'rotate(' + percentageToDegrees(value) + 'deg)')
      } else {
        right.css('transform', 'rotate(180deg)')
        left.css('transform', 'rotate(' + percentageToDegrees(value - 50) + 'deg)')
      }
    }

  })

  function percentageToDegrees(percentage) {

    return percentage / 100 * 360

  }

});

$("#saveButton").click(function (e) {
  $.ajax({
    type: 'POST',
    url: '/update',
    contentType: 'application/json; charset=utf-8',
    data: JSON.stringify({
      url1: $('#url1').text(),
      url2: $('#url2').text(),
      similarity: $('#similarity').text()
    }),
    dataType: 'json',
    success: function(response) {
      console.log(response.redirect)
      window.location.href = response.redirect
    },
    error: function (result) {
      alert('error');
    }
  });
});
