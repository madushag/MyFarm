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
    $('#id_price').attr('step', '0.01');
    $('#id_price').attr('min', '0.0');

    $('#id_min_quantity').attr('step', '0.01');
    $('#id_min_quantity').attr('min', '0.0');
}

function populateInitialValues(){
    $('#id_farm').val($('#farm_id').val())
}

function attachEventHandlers(){

}




