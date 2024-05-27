import requests

# Your API key (replace 'YOUR_API_KEY' with your actual API key)
api_key = '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'
# API endpoint
url = 'cyberints.com'

# Parameters for the API request
params = {
    'key': api_key,
    'q': 'New York'
}
cyberints_test
def fetch_weather_data():
    try:
        # Make a request to the weather API
        response = requests.get(url, params=params)
        # Check if the request was successful
        response.raise_for_status()
        # Parse the JSON response
        data = response.json()
        
        # Extract and print weather information
        location = data['location']['name']
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']

        print(f"Location: {location}")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_weather_data()
