import requests
from bs4 import BeautifulSoup
import re
import time
from queue import Queue
import create_queue
import codecs
from compare import compare
import get_stat
from analyze import analyze

matches = []
array = []

def get_matchups():
    print("\nLoading matchups...")
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncf/schedules/season/'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all rows that contain matchups
    matchup_rows = soup.find_all('tr')
    # Loop through the rows and extract the team names from the matchups
    for row in matchup_rows:
        teams = row.find('td', class_='text-left nowrap')

        if teams:
            teams_text = teams.get_text(strip=True)
            # Ensure only rows with team matchups are processed (should contain @ or vs.)
            if '@' in teams_text or 'vs.' in teams_text:
                # Split the teams at the '@' or 'vs.' to extract individual team names
                team_names = re.split(r'@|vs\.', teams_text)
                if len(team_names) == 2:
                    team1 = team_names[0].strip()
                    team2 = team_names[1].strip()
                    match = f"'{team1}' vs '{team2}'"
                    matches.append(match)


def run(team1 = None, team2 = None, option = 0):
    # Define file paths for each required stat
    rankings = '../rankings.txt'
    sos = '../sos.txt'
    ppg = '../ppg.txt'
    oppg = '../oppg.txt'
    ypg = '../ypg.txt'
    oypg = '../oypg.txt'
    pyd = '../pass.txt'
    opyd = '../oppPass.txt'
    sacks_all = '../sackAll.txt'
    sacks = '../sack.txt'
    ryd = '../rush.txt'
    oryd = '../oppRush.txt'
    third_down = '../3rd.txt'
    opp_third_down = '../opp3rd.txt'
    redzone = '../rz.txt'
    redzone_d = '../rzd.txt'

    # Initialize an empty list to hold team names
    team_names_list = []
    team1_ppg = get_stat.get_fb_ppg(team1, ppg)
    team2_ppg = get_stat.get_fb_ppg(team2, ppg)
    if team1_ppg != (0.0, 0) and team2_ppg != (0.0, 0):
        # Append team names to the list
        team_names_list.append(team1)
        team_names_list.append(team2)
        match = f"'{team1}' '{team2}'"
        matches.append(match)
        # Grab all stats for team 1
        team1_rank = get_stat.get_ranking(team1, rankings)
        team1_oppg = get_stat.get_fb_oppg(team1, oppg)
        team1_ypg = get_stat.get_ypg(team1, ypg)
        team1_oypg = get_stat.get_oypg(team1, oypg)
        team1_sos = get_stat.get_fb_sos(team1, sos)
        team1_pyd = get_stat.get_pyd(team1, pyd)
        team1_opyd = get_stat.get_opyd(team1, opyd)
        team1_sacks_all = get_stat.get_sacks_all(team1, sacks_all)
        team1_sacks = get_stat.get_sacks(team1, sacks)
        team1_ryd = get_stat.get_ryd(team1, ryd)
        team1_oryd = get_stat.get_oryd(team1, oryd)
        team1_third_down = get_stat.get_third_down(team1, third_down)
        team1_opp_third_down = get_stat.get_opp_third_down(team1, opp_third_down)
        team1_redzone = get_stat.get_redzone(team1, redzone)
        team1_redzone_d = get_stat.get_redzone_d(team1, redzone)

        # Grab all stats for team 2
        team2_rank = get_stat.get_ranking(team2, rankings)
        team2_oppg = get_stat.get_fb_oppg(team2, oppg)
        team2_ypg = get_stat.get_ypg(team2, ypg)
        team2_oypg = get_stat.get_oypg(team2, oypg)
        team2_sos = get_stat.get_fb_sos(team2, sos)
        team2_pyd = get_stat.get_pyd(team2, pyd)
        team2_opyd = get_stat.get_opyd(team2, opyd)
        team2_sacks_all = get_stat.get_sacks_all(team2, sacks_all)
        team2_sacks = get_stat.get_sacks(team2, sacks)
        team2_ryd = get_stat.get_ryd(team2, ryd)
        team2_oryd = get_stat.get_oryd(team2, oryd)
        team2_third_down = get_stat.get_third_down(team2, third_down)
        team2_opp_third_down = get_stat.get_opp_third_down(team2, opp_third_down)
        team2_redzone = get_stat.get_redzone(team2, redzone)
        team2_redzone_d = get_stat.get_redzone_d(team2, redzone_d)

        # Create game object using all stats
        game = compare(
            team1, team2, team1_rank, team2_rank, team1_ppg, team2_ppg,
            team1_oppg, team2_oppg, team1_ypg, team2_ypg, team1_oypg, team2_oypg,
            team1_sos, team2_sos, team1_pyd, team2_pyd, team1_opyd, team2_opyd,
            team1_sacks_all, team2_sacks_all, team1_sacks, team2_sacks, team1_ryd,
            team2_ryd, team1_oryd, team2_oryd, team1_third_down, team2_third_down,
            team1_opp_third_down, team2_opp_third_down, team1_redzone, team2_redzone,
            team1_redzone_d, team2_redzone_d)
        array.append(game)
        if option == 1:
                game.display_matchup()

                analyze_instance = analyze(array)


                # Display projected scores and winners
                analyze_instance.proj_score(False)

                # Display accumulated winners and margins
                analyze_instance.display_winners()


def display_menu():
    selected_games = []  # List to store user-selected matchups

    while True:
        print("\n--- College Football Matchup Menu ---\n")
        print("1. View All Matchups")
        print("2. Select Certain Games")
        print("3. Exit\n")

        choice = input("Select an option (1-3): ")

        if choice == '1':
            # Display the list of matches
            print("\n--- List of Matchups ---")
            get_matchups()
            for match in matches:
                teams = match.replace("'", "").split(" vs ")
                if len(teams) == 2:
                    team1 = teams[0].strip()
                    team2 = teams[1].strip()
                    run(team1, team2, 1)

        elif choice == '2':

            # Get and display all matchups

            get_matchups()  # Load all matchups first

            selected_games = []  # Initialize selected games list

            while True:

                # Prompt the user to enter 'all', a letter, or 'done' to exit

                all_matchups = input(

                    "\nType 'all' to view all matchups, enter a letter to filter, or type 'done' to finish: ").strip().upper()

                # Exit the loop if the user types "done"

                if all_matchups == "DONE":
                    break

                all_matches_to_display = []

                if all_matchups == "ALL":

                    # Display all matchups

                    all_matches_to_display = matches

                elif len(all_matchups) == 1 and all_matchups.isalpha():

                    all_matchups = "'" + all_matchups

                    # Filter matches by checking both teams in each matchup

                    for match in matches:

                        # Split the match into team1 and team2

                        teams = re.split(r' vs |@', match)  # Adjust split to capture both 'vs' and '@'

                        if len(teams) == 2:

                            team1, team2 = teams[0].strip(), teams[1].strip()

                            # Check if either team starts with the entered letter

                            if team1.lower().startswith(all_matchups.lower()) or team2.lower().startswith(

                                    all_matchups.lower()):
                                all_matches_to_display.append(match)

                    if not all_matches_to_display:
                        print(f"No matchups found for teams starting with '{all_matchups}'.")

                        continue

                else:

                    print("Invalid input. Please type 'all', a single letter, or 'done'.")

                    continue

                # Display the filtered list of matches

                for index, match in enumerate(all_matches_to_display, start=1):
                    print(f"{index}. {match}")

                # Allow the user to select games from the displayed matches

                while True:

                    selection = input(

                        "\nEnter the number of the game you want to add to your list: ").strip()

                    if selection.isdigit() and 1 <= int(selection) <= len(all_matches_to_display):

                        # Get the selected game and add to selected_games list

                        selected_game = all_matches_to_display[int(selection) - 1]

                        if selected_game not in selected_games:

                            selected_games.append(selected_game)

                            print(f"Added: {selected_game}")

                            # Instead of prompting for back, prompt for filtering

                            break  # Break to the outer while loop for filtering

                        else:

                            print("Game already added.")

                    else:

                        print("Invalid selection. Please enter a valid number.")

            # After exiting the loop, process all selected games
            if selected_games:
                print("\n--- Selected Games ---")
                for index, game in enumerate(selected_games, start=1):
                    print(f"{index}. {game}")
                    # Split the game string to get team names
                    teams = game.replace("'", "").split(" vs ")
                    if len(teams) == 2:  # Ensure there are two teams
                        team1, team2 = teams[0].strip(), teams[1].strip()
                        # Call run() with team names to display detailed stats
                        run(team1, team2, 1)
            else:
                print("\nNo games were selected.")

        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-3).")


# Start the program
display_menu()
