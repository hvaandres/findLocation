import requests

latitude = 39.4225192
longitude = -111.714358
api_key = "b9fa37f868114fd89a08205e42a889e2"

url = f"https://api.opencagedata.com/geocode/v1/json?q=LAT+LNG&key=b9fa37f868114fd89a08205e42a889e2"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Parse the data as needed to extract address information
    results = data.get("results", [])
    if results:
        formatted_address = results[0].get("formatted")
        print("Reverse Geocoded Address:", formatted_address)
    else:
        print("No results found.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
