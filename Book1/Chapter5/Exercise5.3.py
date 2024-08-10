# generating a "post" using request library to obtain Twitter credentials

from Twitter_credentials import b64_encoded_key_secret
import requests

auth_url = "https://api.twitter.com/oauth2/token"

# Information the authorization endpoint wants in order to return an access token to us.
# This includes our encoded key and its data format.
auth_headers = {
    "Authorization": "Basic " + b64_encoded_key_secret,
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
}

auth_data = {
    "grant_type": "client_credentials"
}

# Request the bearer token
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

# Check if the request was successful
if auth_resp.status_code != 200:
    print("Error obtaining bearer token:", auth_resp.status_code, auth_resp.text)
    exit()

# Extract the access token
access_token = auth_resp.json().get('access_token')

if not access_token:
    print("Bearer token not found in response.")
    exit()

# Now that we have an access/bearer token, we're ready to request some data!
search_headers = {
    "Authorization": "Bearer " + access_token
}

# Use the Twitter API v2 search endpoint
search_url = "https://api.twitter.com/2/tweets/search/recent"

# Search parameters
search_params = {
    "query": "Python",
    "max_results": 10
}

# Request tweets
search_resp = requests.get(search_url, headers=search_headers, params=search_params)

# Check if the request was successful
if search_resp.status_code != 200:
    print("Error fetching tweets:", search_resp.status_code, search_resp.text)
    exit()

# Parse the JSON response
Twitter_data = search_resp.json()

# Save the results to a file
with open("Twitter_search_results.json", "w") as Twitter_output_file:
    Twitter_output_file.write(str(Twitter_data))

# Loop through our results and print the text of the Twitter status
for tweet in Twitter_data.get("data", []):  # "data" is the list of Tweets in the JSON object
    print(tweet.get("text", "") + "\n")

