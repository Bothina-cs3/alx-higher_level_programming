$(document).ready(function() {
    $('#btn_translate').click(function() {
        var langCode = $('#language_code').val();
        
        $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function(data) {
            $('#hello').text(data.hello);
        }).fail(function() {
            $('#hello').text('Error: Unable to fetch translation.');
        });
    });
});