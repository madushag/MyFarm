// Test blank JS file

const urlParams = new URLSearchParams(window.location.search);
const produce_filter = urlParams.get('produce');

filter = document.getElementById("produce-filter")

if (filter) {
  if (produce_filter) {
    filter.value = produce_filter
  }
  else {
    filter.value = "ALL"
  }
  
  filter.addEventListener('change', ()=>filter_page(filter.value), false);
  
  function filter_page(filter_value) {
    const filter_url = "/?produce=" + filter_value
    document.location.href = filter_url
  }  
}
