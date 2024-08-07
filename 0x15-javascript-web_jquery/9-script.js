$(document).ready(function() {
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        const helloMessage = data.hello;
        $('#hello').text(helloMessage);
    });
});
