import requests

# Your Yelp API key
API_KEY = 'YOUR_API_KEY_HERE'

# Base URL for Yelp API
BASE_URL = 'https://api.yelp.com/v3/'

# API Endpoint for searching for businesses
SEARCH_PATH = 'businesses/search'

# Query parameters for the search
SEARCH_PARAMS = {
    'term': 'food',
    'location': 'San Francisco, CA',
    'limit': 50
}

# Set the headers for the request
HEADERS = {
    'Authorization': f"Bearer {API_KEY}"
}

# Make the request to the Yelp API
response = requests.get(BASE_URL + SEARCH_PATH, params=SEARCH_PARAMS, headers=HEADERS)

# Print the status code of the response
print(response.status_code)

# Print the response data
print(response.json())
