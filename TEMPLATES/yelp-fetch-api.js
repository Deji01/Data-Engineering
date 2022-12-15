const API_KEY = "your_api_key_here";
const API_ENDPOINT = "https://api.yelp.com/v3/businesses/search";

const params = new URLSearchParams({
  term: "food",
  location: "San Francisco"
});

fetch(`${API_ENDPOINT}?${params}`, {
  method: "GET",
  headers: {
    Authorization: `Bearer ${API_KEY}`
  }
})
  .then(response => response.json())
  .then(json => {
    const businesses = json.businesses;
    for (const business of businesses) {
      console.log(business.name);
    }
  })
  .catch(error => {
    console.error(error);
  });
