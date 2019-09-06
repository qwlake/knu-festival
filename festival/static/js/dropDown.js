$(document).ready(function(){
    $(".item1").hide()
    var state = 1;
    $(".dropMenu").click(function (){
        if (state == 1){
            $(this).parent().find(".subNav").slideDown('normal').show();
            $(".item1").show()
            state = state + 1;
        }else{
            $(this).parent().find(".subNav").slideUp('fast');
            state = state - 1;
        }
    })
})