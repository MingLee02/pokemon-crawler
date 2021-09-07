$(document).ready(function() {
    $("#toggle-pokemon-screen").on('click tap', function() {
        if ($(this).text() == '>>') {
            $('.page-2').removeClass('d-none');
            $('.page-1').addClass('d-none');
            $(this).text('<<');
        } else {
            $('.page-2').addClass('d-none');
            $('.page-1').removeClass('d-none');
            $(this).text('>>');
        }
    });
});