// Test blank JS file

const urlParams = new URLSearchParams(window.location.search);
const produce_query = urlParams.get('produce');

produce_filter = document.getElementById("produce-filter")

if (produce_filter) {
  if (produce_query) {
    produce_filter.value = produce_query
  }
  
  produce_filter.addEventListener('change', ()=>filter_page(produce_filter.value), false);
  
  function filter_page(filter_value) {
    const filter_url = "/?produce=" + filter_value
    document.location.href = filter_url
  }  
}
