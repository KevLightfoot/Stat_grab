import requests
from bs4 import BeautifulSoup
import re
import baseball_stats

# URL of the webpage containing the matchups
url = 'https://d1baseball.com/scores'
# Make a request to the webpage
html_content = requests.get(url).text
# Parse the HTML content of the webpage
soup = BeautifulSoup(html_content, 'html.parser')

# Find all matchups
away_teams = soup.find_all(class_='team-1')
home_teams = soup.find_all(class_='team-2')

# Set to store unique team names
unique_teams = set()

# List to store matchups
all_matchups = []

# Print each game in the specified format
for away_team, home_team in zip(away_teams, home_teams):
    away_name = away_team.find(class_='team-title').text.strip()
    home_name = home_team.find(class_='team-title').text.strip()

    # Use regular expression to strip off ranking if present
    away_name = re.sub(r'^\d+\s', '', away_name)
    home_name = re.sub(r'^\d+\s', '', home_name)

    # Check if both away and home team names are unique
    if away_name not in unique_teams and home_name not in unique_teams:
        away_rank = baseball_stats.find_rank(away_name)
        home_rank = baseball_stats.find_rank(home_name)
        away_record = baseball_stats.find_record(away_name)
        home_record = baseball_stats.find_record(home_name)

        # Assign a large number for teams with rank 0
        away_rank = 999 if away_rank[0] == 0 else away_rank[0]
        home_rank = 999 if home_rank[0] == 0 else home_rank[0]

        # Check if records are not None
        if away_record is not None and home_record is not None:
            matchup = (away_name, away_record, home_name, home_record, away_rank, home_rank)
            all_matchups.append(matchup)
            unique_teams.add(away_name)
            unique_teams.add(home_name)

# Sort matchups based on the maximum difference in wins between the two teams
sorted_matchups = sorted(all_matchups, key=lambda x: max(abs(int(x[1].split('-')[0]) - int(x[3].split('-')[0])), abs(int(x[1].split('-')[1]) - int(x[3].split('-')[1]))), reverse=True)

# Iterate through sorted matchups and replace ranks of 999 with "Non D1"
for i, matchup in enumerate(sorted_matchups):
    sorted_matchups[i] = (
    matchup[0], matchup[1], matchup[2], matchup[3], "Non D1" if matchup[4] == 999 else matchup[4],
    "Non D1" if matchup[5] == 999 else matchup[5])

# Print sorted matchups
for matchup in sorted_matchups:
    away_name, away_record, home_name, home_record, away_rank, home_rank = matchup
    print(f"{away_rank} {away_name} ({away_record}) @ {home_rank} {home_name} ({home_record})")
    print("\n______________________________________________________________________________________\n")
