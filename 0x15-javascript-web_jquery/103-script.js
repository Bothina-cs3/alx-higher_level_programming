$(document).ready(function() {
    function fetchTranslation() {
        var langCode = $('#language_code').val();
        
        $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function(data) {
            $('#hello').text(data.hello);
        }).fail(function() {
            // Handle error if the request fails
            $('#hello').text('Error: Unable to fetch translation.');
        });
    }
    
    $('#btn_translate').click(fetchTranslation);
    
    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            fetchTranslation();
        }
    });
});