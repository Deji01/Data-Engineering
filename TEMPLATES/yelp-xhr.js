const API_KEY = "your_api_key_here";
const API_ENDPOINT = "https://api.yelp.com/v3/businesses/search";

// Set up the HTTP request
const xhr = new XMLHttpRequest();
xhr.responseType = "json";
xhr.onreadystatechange = () => {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    // Process the response from the Yelp API
    const businesses = xhr.response.businesses;
    for (const business of businesses) {
      console.log(business.name);
    }
  }
};

// Set the HTTP method and endpoint
xhr.open("GET", `${API_ENDPOINT}?term=food&location=San+Francisco`);

// Set the authorization header with the API key
xhr.setRequestHeader("Authorization", `Bearer ${API_KEY}`);

// Send the request
xhr.send();
