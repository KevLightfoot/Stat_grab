import requests
from bs4 import BeautifulSoup

# Create a session
session = requests.Session()
try:
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncf/schedules/season/'
    html_content = session.get(url).text  # Use the session to make the request
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all rows that contain matchups
    matchup_rows = soup.find_all('tr')
finally:
    session.close()  # Ensure that all connections are closed when done