function setFieldStyles(){
    $('input[id^="id"], textarea[id^="id"]').each(function() {
        $(this).addClass('form-control');

        if($(this).attr('id').indexOf('name') > 0){
            $(this).attr({'placeholder': 'Name of farm'});
        }
        if($(this).attr('id').indexOf('description') > 0){
            $(this).attr({'placeholder': 'Description of farm'});
        }
        if($(this).attr('id').indexOf('phone') > 0){
            $(this).attr({'placeholder': 'Phone number of farm as 123-456-7890'});
        }
         if($(this).attr('id').indexOf('website') > 0){
            $(this).attr({'placeholder': 'Farm website URL'});
        }
    });

    //  $('select[id^="id"]').each(function() {
    //     $(this).addClass('form-select');
    // });

    // $('#id_city').hide();
    // $('#id_location_state').hide();
    // $('label[for="id_location_state"]').hide()
    // $('label[for="id_city"]').hide()

}

function enableFieldValidations(){
    $('#id_phone_no').attr('oninvalid', 'this.setCustomValidity("Enter a valid phone number using format 123-456-7890")');
    $('#id_phone_no').attr('oninput', "this.setCustomValidity('')");
    $('#id_phone_no').attr('pattern', "[0-9]{3}-[0-9]{3}-[0-9]{4}");

    if($('#id_location_state').val() === '-1')
        $('#id_city').prop('disabled', true);
}

function populateInitialValues(){
    // If there is a location, then show the location address details
    if($('#id_location_name').val()){
        $('#id_location').val($('#id_location_name').val());
        $('#id_address_link').html($('#id_location_address').val());
        $('#id_address_link').attr('href', $('#id_location_url').val());
        $('#id_view_in_google').html("(Click to view in Google Maps)");
        $('#id_view_in_google').attr('href', $('#id_location_url').val());
        $("label[for='id_address']").show();

    }
}

function attachEventHandlers(){
    $('#id_location_state').on('change',()=>{
        if($('#id_location_state').val() === '-1') {
            $('#id_city').val('');
            $('#id_city').prop('disabled', true);
        }
        else
            $('#id_city').prop('disabled', false);
    });
}




