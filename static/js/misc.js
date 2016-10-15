/**
 * Created by Daemon on 4/18/2016.
 */

$(document).ready(function(){
    $('.intro').css('height',$(window).height());
    $('.contact').css('height',$(window).height());
    $('.demo').css('height',$(window).height());


    $('#submit').click(function(){
        $('#error').text('');
        var name=$('#name').val();
        var number=$('#number').val();
        if(name=="" || number=="") {
            $('#error').text('Please enter the details');
            return;
        }

        $('#error').css('display','inline');
        $.ajax({
            type: "POST",
            url: "php/subscribe.php",
            data: {"name":name,"number":number},
            success: function(result) {
                $('#error').text(result);
                console.log(result);
                $('#loader').css('display','none');
            },
            failure: function(result){
                $('#error').text(result);
                console.log(result);
                $('#loader').css('display','none');
            }
        });
    });

});

$(window).resize(function(){
    $('.intro').css('height',$(window).height());
    $('.contact').css('height',$(window).height());
    $('.demo').css('height',$(window).height());
});

$(window).scroll(function() {
    if ($(window).scrollTop() > 600) {
        $("#navmain").css("transform","translateY(0px)");
    }
    else{
        $("#navmain").css("transform","translateY(-60px)");
    }
});