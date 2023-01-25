window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const language_code = $('INPUT#language_code').val();
    $.get ('https://www.fourtonfish.com/hellosalut/hello/' + language_code, function (data, status) {
      $('DIV#hello').text(data.hello);
    });
  });
});
