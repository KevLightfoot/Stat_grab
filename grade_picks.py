import requests
from bs4 import BeautifulSoup
from queue import Queue
import re
losers = list()
winners = list()

bet = input("Pick one\n1. Moneyline\n2. Spread\n")

# Hardcode projected winners
proj_winners = ['Tulane', 'Maryland', 'Iowa St', 'DePaul', 'Texas A&M', 'Oklahoma', 'Geo Mason',
                'UCLA', 'Pittsburgh', 'Virginia', 'Florida', 'Alabama', 'Wash State', 'Ohio St',
                'S Methodist', 'N Alabama', 'Marquette', 'Rutgers', 'Notre Dame', 'Furman', 'Butler',
                'Citadel', 'Austin Peay', 'Purdue', 'VA Tech', 'Missouri', 'Marshall', 'Hawaii',
                'Air Force', 'CS Bakersfld']

if bet == "1":
    url = 'https://www.teamrankings.com/ncaa-basketball-win-picks'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')

    results = Queue()
    results.put(soup.prettify())
    results = BeautifulSoup(results.get(), 'html.parser')

    # Extract losers
    team_name = results.find("span", class_="dark_red").find_next("td").find("a")
    while team_name:
        team1 = team_name.text.strip()
        losers.append(team1)
        try:
            team_name = team_name.find_next("span", class_="dark_red").find_next("td").find("a")
        except AttributeError:
            break

    # Extract winners
    team_name = results.find("span", class_="dark_green").find_next("td").find("a")
    while team_name:
        vs = team_name.find_next('td').text
        team1 = team_name.text.strip()
        team2 = vs.strip().replace("vs ", '').replace("at ", '')
        winners.append((team1, team2))
        try:
            team_name = team_name.find_next("span", class_="dark_green").find_next("td").find("a")
        except AttributeError:
            break

    # Analyze picks based on projected winners
    updated_winners = []
    for team in proj_winners:
        if team in losers:
            updated_winners.append(team + " - loss")
        elif any(team == winner[1] for winner in winners):
            updated_winners.append(team + " - loss")
        else:
            updated_winners.append(team + " - win")

    # Display results
    for item in updated_winners:
        print(item)

    win_count = sum("win" in team for team in updated_winners)
    loss_count = sum("loss" in team for team in updated_winners)
    print(f"Record: {win_count}-{loss_count}")

elif bet == "2":
    url = 'https://www.teamrankings.com/ncaa-basketball-ats-picks/'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')

    rows = soup.find_all("tr", class_=re.compile(r"team_\d+"))
    extra_wins = 0
    extra_losses = 0
    spread_results = []

    # Extract team names, spreads, and whether they were right or wrong
    for row in rows:
        result_status = row.find("span", class_=["dark_red", "dark_green"])
        if result_status:
            outcome = "Right" if "dark_green" in result_status["class"] else "Wrong"

            # Extract the team and spread info
            spread_info = row.find("a").text.strip()
            team, spread = spread_info.split(maxsplit=1)
            spread_results.append((team, spread, outcome))

    ats_winners = []
    unclear_teams = []

    # Analyze the extracted spread data
    for team in proj_winners:
        matched = False
        for spread_team, spread, outcome in spread_results:
            if team == spread_team:
                if outcome == "Right":
                    ats_winners.append(f"{team} - win")
                else:
                    ats_winners.append(f"{team} - loss")
                matched = True
                break

        if not matched:
            unclear_teams.append(team)

    # Count extra wins and losses for teams not in your list
    for spread_team, spread, outcome in spread_results:
        if spread_team not in proj_winners:
            if outcome == "Right":
                extra_losses += 1
            else:
                extra_wins += 1

    # Assign extra wins/losses to unclear teams
    for team in unclear_teams:
        if extra_wins > 0:
            ats_winners.append(f"{team} - win")
            extra_wins -= 1
        else:
            ats_winners.append(f"{team} - loss")
            extra_losses -= 1

    # Display results
    for item in ats_winners:
        print(item)

    win_count = sum("win" in team for team in ats_winners)
    loss_count = sum("loss" in team for team in ats_winners)
    print(f"Record: {win_count}-{loss_count}")




