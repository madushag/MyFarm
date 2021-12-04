// Test blank JS file
//
const urlParams = new URLSearchParams(window.location.search);
let produceFilter = urlParams.get('produce');
let saleTypeFilter = urlParams.get('saleType');
let distanceFilter = urlParams.get('distance');

// const produce_query = urlParams.get('produce');
// produce_filter = document.getElementById("produce-filter")
//
// if (produce_filter) {
//     if (produce_query) {
//         produce_filter.value = produce_query
//     }
// }
//
//   produce_filter.addEventListener('change', ()=>filter_page(produce_filter.value), false);
//
//   function filter_page(filter_value) {
//     const filter_url = "/?produce=" + filter_value
//     document.location.href = filter_url
//   }
// }


function attachEventHandlers(){
   $('#btn_search').click(filter_page);
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

    if(localStorage.getItem('customer_address')){
        $('#id_customer_location').val(localStorage.getItem('customer_address'))
    }
}

function filter_page() {
    if($('#id_customer_location').val()) {
        let produce_filter = $('#produce-filter').val();
        let saleType_filter = $('#sale-type-filter').val();
        let distance_filter = $('#distance-filter').val();

        if(produce_filter !== 'Any') {
            produce_filter = produce_filter.toLowerCase();
        }
        let filter_url = "/?1=1" + (produce_filter !== 'Any' ? "&produce=" + produce_filter.toUpperCase() : '')
                                + (saleType_filter !== 'Any' ? "&saleType=" + saleType_filter : '')
                                + (distance_filter !== '-1' ? "&distance=" + distance_filter : '')
                                + (localStorage.getItem('customer_lng') ? "&lng=" + localStorage.getItem('customer_lng') + "&lat=" + localStorage.getItem('customer_lat') : '') ;
        document.location.href = filter_url;
    }
    else{
        alert("Please specify your location!")
    }
  }