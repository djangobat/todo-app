$(function(){

    function updateList(e) {
        $('.todo-list ul li a').each(function( index ) {
            if ($(this).text().toLowerCase().indexOf(log.toLowerCase()) >= 0) {
                $(this).fadeIn(300);
            } else {
                $(this).fadeOut(300);
            }
        });
    }
    
    $('.todo-list ul li a input[type="checkbox"]').change(function() {
        if($(this).prop('checked') > 0) {
            $(this).parent().addClass('done');
        } else {
            $(this).parent().removeClass('done');
        }
    });

});