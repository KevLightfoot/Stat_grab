import requests

# Dictionary with URLs as keys and corresponding file names as values
urls_to_files = {
    'https://www.teamrankings.com/college-football/ranking/predictive-by-other': 'rankings.txt',
    'https://www.teamrankings.com/college-football/stat/points-per-game': 'ppg.txt',
    'https://www.teamrankings.com/college-football/stat/opponent-points-per-game': 'oppg.txt',
    'https://www.teamrankings.com/college-football/stat/yards-per-game': 'ypg.txt',
    'https://www.teamrankings.com/college-football/stat/opponent-yards-per-game': 'oypg.txt',
    'https://www.teamrankings.com/college-football/ranking/season-sos-by-other': 'sos.txt',
    'https://www.teamrankings.com/college-football/stat/passing-yards-per-game': 'pass.txt',
    'https://www.teamrankings.com/college-football/stat/opponent-passing-yards-per-game': 'oppPass.txt',
    'https://www.teamrankings.com/college-football/stat/rushing-yards-per-game': 'rush.txt',
    'https://www.teamrankings.com/college-football/stat/opponent-rushing-yards-per-game': 'oppRush.txt',
    'https://www.teamrankings.com/college-football/stat/third-down-conversion-pct': '3rd.txt',
    'https://www.teamrankings.com/college-football/stat/opponent-third-down-conversion-pct': 'opp3rd.txt',
    'https://www.teamrankings.com/college-football/stat/qb-sacked-pct': 'sackAll.txt',
    'https://www.teamrankings.com/college-football/stat/sack-pct': 'sack.txt',
    'https://www.teamrankings.com/college-football/ranking/season-sos-by-other': 'sos.txt',
    'https://www.teamrankings.com/college-football/stat/sack-pct': 'rz.txt',
    'https://www.teamrankings.com/college-football/ranking/season-sos-by-other': 'rzd.txt'
}

# Loop through each URL, retrieve the HTML, and save it to a file in the current directory
for url, filename in urls_to_files.items():
    try:
        # Get the HTML content of the page
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful

        # Write the HTML content to the corresponding file in the current directory
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"Saved HTML content from {url} to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url}. Error: {e}")
