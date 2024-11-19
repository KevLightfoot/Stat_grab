import requests

# URL of the webpage you want to download the HTML from
url = 'https://barttorvik.com/#'

# Send a GET request to fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open the file in write mode and save the HTML content
    with open('bart.txt', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("HTML content has been saved to bart.txt.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
