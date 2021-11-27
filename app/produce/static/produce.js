function setFieldStyles(){
    $('input[id^="id"], textarea[id^="id"]').each(function() {
        $(this).addClass('form-control');

        if($(this).attr('id').indexOf('name') > 0){
            $(this).attr({'placeholder': 'Name produce'});
        }
        if($(this).attr('id').indexOf('price') > 0){
            $(this).attr({'placeholder': 'Price per lb'});
        }
        if($(this).attr('id').indexOf('min_quantity') > 0){
            $(this).attr({'placeholder': 'Minimum quantity for sale in lbs'});
        }
    });

    $('input[type="checkbox"]').each(function() {
        $(this).addClass('form-check-input');
    })

}

function enableFieldValidations(){
}

function populateInitialValues(){
    $('#id_farm').val($('#farm_id').val())
}

function attachEventHandlers(){

}




