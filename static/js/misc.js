/**
 * Created by Daemon on 4/18/2016.
 */

words=['Focussed','Skilled','Determined','Started'];

$(document).ready(function(){
    $('.about').css('height',$(window).innerHeight());
    $('.contact').css('height',$(window).innerHeight());
    $('.sphere').css('height',$(window).innerHeight());

    setInterval(function(){setslogan("random");},4000);
    setInterval(function(){setslogan("random2");},3000);


   

});



function setslogan(e){
    $("#"+e).fadeOut(300);
    x=Math.floor((Math.random()*$(window).innerWidth()-100)+100);
    y=Math.floor((Math.random()*$(window).innerHeight()-100)+100);
    fontsize=Math.ceil((Math.random()*40)+10);
    index=Math.floor(Math.random()*words.length);
    setTimeout(function(){
        $("#"+e).css('top',y);
        $("#"+e).css('left',x);
        $("#"+e).css('font-size',fontsize);
        $("#"+e).text(words[index]);
        $("#"+e).fadeIn(300);
    },500);
}

function conditional_collapse(){
    if($(window).innerWidth()<600) {
        $('.navbar-toggle').click();
        console.log($(window).innerWidth());
    }
}


function subscribe(){
        email=$('.subscribe-text').val();
        if(email=="")
        {
            $('#message').fadeIn(300);
            $('#message').text('Email Please');
            setTimeout(function(){ clear();},1000);
            return;
        }
        $('#loader').fadeIn(300);
        $.ajax({
            url:"/subscribe/",
            data:{email:email},
            type:'post',
            success:function(response){
                $('#loader').hide();
                $('#message').text(response);
                $('#message').fadeIn(300);
                setTimeout(function(){ clear();},3000);
            },
            failure:function(response){
                $('#loader').hide();
                $('#message').text('Oops.! Something went wrong.');
                $('#message').fadeIn(300);
                setTimeout(function(){ clear();},3000);
            }

        });
    }

    function clear(){
        $('#message').fadeOut(300);
        $('#message').text('');
    }

    function contact_clear(){
        $('#contact-message').fadeOut(300);
        $('#contact-message').text('');
        $('#contact-name').val('');
        $('#contact-email').val('');
        $('#contact-query').val('');
    }

    function submit_query(){
        name=$('#contact-name').val();
        email=$('#contact-email').val();
        query=$('#contact-query').val();
        if(email=="" || name=="" || query=="")
        {
            $('#contact-message').fadeIn(300);
            $('#contact-message').text('Something appears to be missing');
            setTimeout(function(){ contact_clear();},1000);
            return;
        }
        $('#contact-loader').fadeIn(300);
        $.ajax({
            url:"/query/",
            data:{email:email,name:name,query:query},
            type:'post',
            success:function(response){
                $('#contact-loader').hide();
                $('#contact-message').text(response);
                $('#contact-message').fadeIn(300);
                setTimeout(function(){ contact_clear();},3000);
            },
            failure:function(response){
                $('#contact-loader').hide();
                $('#contact-message').text('Oops.! Something went wrong.');
                $('#contact-message').fadeIn(300);
                setTimeout(function(){ contact_clear();},3000);
            }

        });
    }