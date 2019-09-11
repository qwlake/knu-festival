$(document).ready(function(){
    $(".item1").hide()
    var state = 1;
    $(".dropMenu").click(function (){
        if (state == 1){
            $(this).parent().find(".subNav").slideDown('normal').show();
            $(".item1").show();
            $(".contentSection").toggleClass("contentDiv");
            state = state + 1;
        }else{
            $(this).parent().find(".subNav").slideUp('normal');
            $(".contentSection").toggleClass("contentDiv");
            state = state - 1;
        }
    })
})