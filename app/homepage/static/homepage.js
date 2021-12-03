// Test blank JS file
//
const urlParams = new URLSearchParams(window.location.search);
const produce_query = urlParams.get('produce');
produce_filter = document.getElementById("produce-filter")

if (produce_filter) {
    if (produce_query) {
        produce_filter.value = produce_query
    }
}
//
//   produce_filter.addEventListener('change', ()=>filter_page(produce_filter.value), false);
//
//   function filter_page(filter_value) {
//     const filter_url = "/?produce=" + filter_value
//     document.location.href = filter_url
//   }
// }


// function attachEventHandlers(){
//     $('#produce_filter').on('change',()=>{
//         $('#filter_criteria').val($('#produce_filter').val())
//     })
//     });
// }

function storeCustomerLocationInLocalStorage(place){
    localStorage.setItem('customer_address', place.formatted_address);
    localStorage.setItem('customer_lat', place.geometry.location.lat());
    localStorage.setItem('customer_lng', place.geometry.location.lng());
}

function populateInitialValues(){
    if(localStorage.getItem('customer_address')){
        $('#id_customer_location').val(localStorage.getItem('customer_address'))
    }
}

function filter_page() {
    if($('#id_customer_location').val()) {
        let produce_filter = $('#produce-filter').val();
        let distance_filter = $('#distance-filter').val();
        const filter_url = "/?produce=" + produce_filter + "&distance=" + distance_filter + "&lng=" + localStorage.getItem('customer_lng') + "&lat=" + localStorage.getItem('customer_lat');
        document.location.href = filter_url;
    }
    else{
        alert("Please specify a location")
    }
  }