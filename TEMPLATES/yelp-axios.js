const axios = require("axios");

const API_KEY = "your_api_key_here";
const API_ENDPOINT = "https://api.yelp.com/v3/businesses/search";

const params = {
  term: "food",
  location: "San Francisco"
};

const headers = {
  Authorization: `Bearer ${API_KEY}`
};

axios
  .get(API_ENDPOINT, { params, headers })
  .then(response => {
    const businesses = response.data.businesses;
    for (const business of businesses) {
      console.log(business.name);
    }
  })
  .catch(error => {
    console.error(error);
  });
