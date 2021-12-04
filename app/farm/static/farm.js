function wireUpGoogleAutoComplete(input, options) {
    const autocomplete = new google.maps.places.Autocomplete(input, options);
    autocomplete.addListener("place_changed", ()=> {
        let place = autocomplete.getPlace();
        let address_comps = place.address_components;
        let address_location = place.geometry.location;

        let route = address_comps.find(obj => obj.types.includes("route"));
        let locality = address_comps.find(comp => comp.types.includes("locality"));
        let sublocality = address_comps.find(comp => comp.types.includes("sublocality"));
        let state = address_comps.find(comp => comp.types.includes("administrative_area_level_1")).short_name;
        let country = address_comps.find(comp => comp.types.includes("country")).long_name;

        let street = "";
        if (route){
            street = route.long_name;
        }

        if (!locality && sublocality)
            $('#id_city').val(sublocality.long_name);
        else if(locality)
            $('#id_city').val(locality.long_name);
        else
            $('#id_city').val('');

        $('#id_location_state').val();
        $('#id_location_lat').val(address_location.lat());
        $('#id_location_lng').val(address_location.lng().toFixed(13));
        $("label[for='id_address']").show();
        $('#id_address_link').html(place.formatted_address);
        $('#id_address_link').attr('href', place.url);
        $('#id_view_in_google').html("(Click to view in Google Maps)");
        $('#id_view_in_google').attr('href', place.url);

        $('#id_location_name').val(place.name
                                + (route ? ", " + street : "")
                                + ($('#id_city').val() ? ", " + $('#id_city').val() : '')
                                + ", " + state
                                + ", " + country);

        $('#id_location_url').val(place.url);
        $('#id_location_address').val(place.formatted_address);

        $('#id_name').val(place.name);
    });
}

function setFieldStyles(){
    $('input[id^="id"], textarea[id^="id"]').each(function() {
        $(this).addClass('form-control');

        if($(this).attr('id').indexOf('name') > 0){
            $(this).attr({'placeholder': 'Name of point of sale location, e.g. "Lincoln Farmer\'s Market"'});
        }
        if($(this).attr('id').indexOf('farm_name') > 0){
            $(this).attr({'placeholder': 'Display name for your farm, e.g. "Dave\'s organic veg farm"'});
        }
        if($(this).attr('id').indexOf('description') > 0){
            $(this).attr({'placeholder': 'Description of point of sale'});
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




