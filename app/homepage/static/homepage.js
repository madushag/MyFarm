
const urlParams = new URLSearchParams(window.location.search);
let produceFilter = urlParams.get('produce');
let saleTypeFilter = urlParams.get('saleType');
let distanceFilter = urlParams.get('distance');
let organicFilter = urlParams.get('organic');


function attachEventHandlers(){
   $('#btn_search').click(filter_page);

   $('#btn_clear_customer_location').click(()=>{
        localStorage.removeItem('customer_address');
        localStorage.removeItem('customer_lat');
        localStorage.removeItem('customer_lng');
        $('#id_customer_location').val('');
   });
}

function storeCustomerLocationInLocalStorage(place){
    localStorage.setItem('customer_address', place.formatted_address);
    localStorage.setItem('customer_lat', place.geometry.location.lat());
    localStorage.setItem('customer_lng', place.geometry.location.lng());
}


function populateInitialValues(){
    if(produceFilter) {
        $('#produce-filter').val(produceFilter);
    }
    if(saleTypeFilter) {
        $('#sale-type-filter').val(saleTypeFilter);
    }
    if(distanceFilter) {
        $('#distance-filter').val(distanceFilter);
    }
    if(organicFilter == 'true') {
        $('#organic_type_filter').prop('checked', true);
    }
    // populate the customer location if one is available
    if(localStorage.getItem('customer_address')){
        $('#id_customer_location').val(localStorage.getItem('customer_address'))
    }
}

function filter_page() {

    if($('#id_customer_location').val() || $('#distance-filter').val() === '-1'){

        let produce_filter = $('#produce-filter').val();
        let saleType_filter = $('#sale-type-filter').val();
        let distance_filter = $('#distance-filter').val();
        let organic_filter = $("#organic_type_filter").prop("checked");
        if(produce_filter !== 'Any') {
            produce_filter = produce_filter.toLowerCase();
        }

        let filter_url = "/?1=1" + (produce_filter !== 'Any' ? "&produce=" + produce_filter.toUpperCase() : '')
                                + (saleType_filter !== 'Any' ? "&saleType=" + saleType_filter : '')
                                + (organic_filter !== 'Any' ? "&organic=" + organic_filter : '')
                                + (distance_filter !== '-1' ? "&=" + distance_filter : '')
                                + (localStorage.getItem('customer_lng') ? "&lng=" + localStorage.getItem('customer_lng') + "&lat=" + localStorage.getItem('customer_lat') : '') ;
        document.location.href = filter_url;
    }
    else{
        alert("Please specify your location!")
    }
  }
