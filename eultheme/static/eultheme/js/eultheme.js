$(document).ready(function(){

    /* advanced search filter controls */
    function toggleGroup(elem){
        var $this = $(elem),
        group = $this.attr('data-type');

        $this.toggleClass('active');
        $(".group[data-type='"+ group +"']").stop(false,true).slideToggle(500);

    }

    var $toggleSwitch = $('.toggle.switch');
    if($toggleSwitch.length>0){
        $toggleSwitch.on('click',function(e){
            e.preventDefault();
            toggleGroup(this);
        });
    }

    $advOptionsGroup =  $(".adv.group");

    $('.adv.group .controls .btn').bind('click', function(e){
        e.preventDefault();

        var $this = $(this);
        if($this.hasClass('submit')){
            search.get();
        }
        else if($this.hasClass('reset')){
            reset($advOptionsGroup);
        }
    });

    function reset(elem){
        var $elem = $(elem),
        $inputs = $elem.find('input');
        $inputs.attr('value','').val('');
    }


    /* NOTE: also requires inclusion of  eultheme/js/bootstrap-datepicker.js */
    $("#date-range input").datepicker({
        format: "yyyy",
        viewMode: "years",
        minViewMode: "years"
    });


});
