function setFieldStyles(){
    $('input[id^="id"], textarea[id^="id"]').each(function() {
        $(this).addClass('form-control');

        if($(this).attr('id').indexOf('name') > 0){
            $(this).attr({'placeholder': 'Name produce'});
        }
        if($(this).attr('id').indexOf('price') > 0){
            $(this).attr({'placeholder': 'Price per unit'});
        }
        if($(this).attr('id').indexOf('min_quantity') > 0){
            $(this).attr({'placeholder': 'Minimum quantity for sale'});
        }
    });

    $('select').each(function() {
        $(this).addClass('form-select');
    })

    $('input[type="checkbox"]').each(function() {
        $(this).addClass('form-check-input');
    })

}

function enableFieldValidations(){
    let priceElement =$('#id_price');
    priceElement.attr('step', '0.01');
    priceElement.attr('min', '0.0');

    $('#id_min_quantity').attr('step', '0.01');
    $('#id_min_quantity').attr('min', '0.0');
}

function populateInitialValues(){
    console.log($('#farm_id').val());
    $('#id_farm').val($('#farm_id').val())
}

function attachEventHandlers(){

}




