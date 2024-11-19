import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import create_queue
import get_stat
import time
from matchups import matchups
from project import Project


all_matchups = []
print("\nThinking...\n\n\n")
start_time = time.time()
queue_start = time.time()

# URL of the webpage containing the matchups
url = 'https://www.teamrankings.com/ncb/schedules'
# Make a request to the webpage
html_content = requests.get(url).text
# Parse the HTML content of the webpage
soup = BeautifulSoup(html_content, 'html.parser')
#initialize and populate Queue
matchup_queue = Queue()
matchup_queue.put(soup.prettify())
soup = BeautifulSoup(matchup_queue.get(), 'html.parser')
# Find all 'td' elements with class 'text left nowrap'
td_elements = soup.find_all('td', class_='text-left nowrap')


#Create all necesary Queues
sos = create_queue.sos()
ppg = create_queue.bb_ppg()
opp_ppg = create_queue.opp_ppg()
eff_fg_perc = create_queue.eff_fg_perc()
opp_eff_fg_perc = create_queue.opp_eff_fg_perc()
rebound_perc = create_queue.rebound_perc()
possesions = create_queue.possesions()
eff_poss_ratio = create_queue.eff_poss_ratio()
opp_eff_poss_ratio = create_queue.opp_eff_poss_ratio()
three_perc = create_queue.three_perc()
perc_fr_three = create_queue.perc_fr_three()
opp_three = create_queue.opp_three()
home_rating = create_queue.home_rating()
away_rating = create_queue.away_rating()
l5_rating = create_queue.l5_rating()


#Mark time taken
queue_stop = time.time()

#start time for all calls
call_start = time.time()
matchups_list = list()
summary = list()
total = int(0)
# Print the text content of each link and its surrounding text
for td in td_elements:
    # Find all 'a' elements that contain '/some-page' in the 'href' attribute
    links = td.find_all('a', href=lambda x: '/ncaa-basketball/matchup' in x)
    for link in links:
        total = int(0)
        # Store matchup info in a list
        curr = re.findall(r'#\d+\s+(.+?)\s+(?:at|vs\.)\s+#\d+\s+(.+)', link.text)

        #print(curr)
        if curr:
            team1 = curr[0][0].strip()
            team2 = curr[0][1]
            print(f"{team1} vs {team2}")

            #print(f"{link.text.strip()}\n")
            ranks = link.text.strip()
            matchranks = re.findall(r'#(\d+)', ranks)

            # Extract the first and second numbers
            team1_rank = int(matchranks[0]) if matchranks else None
            team2_rank = int(matchranks[1]) if len(matchranks) > 1 else None

        #get teams sos
        team1_sos = get_stat.get_sos(curr[0][0].strip(), sos)
        team2_sos = get_stat.get_sos(curr[0][1], sos)

        #get teams PPG
        team1_ppg = get_stat.get_bb_ppg(curr[0][0].strip(), ppg)
        team2_ppg = get_stat.get_bb_ppg(curr[0][1], ppg)

        #get teams OPPG
        team1_opp_ppg = get_stat.get_opp_ppg(curr[0][0].strip(), opp_ppg)
        team2_opp_ppg = get_stat.get_opp_ppg(curr[0][1], opp_ppg)

        #get teams EFG
        team1_eff_fg_perc = get_stat.get_eff_fg_perc(curr[0][0].strip(), eff_fg_perc)
        team2_eff_fg_perc = get_stat.get_eff_fg_perc(curr[0][1], eff_fg_perc)

        #get teams OEFG%
        team1_opp_eff_fg_perc = get_stat.get_opp_eff_fg_perc(curr[0][0].strip(), opp_eff_fg_perc)
        team2_opp_eff_fg_perc = get_stat.get_opp_eff_fg_perc(curr[0][1], opp_eff_fg_perc)


        #get teams rebound rate
        team1_reb_rate = get_stat.get_opp_eff_fg_perc(curr[0][0].strip(), rebound_perc)
        team2_reb_rate = get_stat.get_opp_eff_fg_perc(curr[0][1], rebound_perc)

        # get eff_poss_ratio
        team1_eff_poss_ratio = get_stat.get_eff_pos_ratio(curr[0][0].strip(), eff_poss_ratio)
        team2_eff_poss_ratio = get_stat.get_eff_pos_ratio(curr[0][1], eff_poss_ratio)

        # get opp_eff_poss_ratio
        team1_opp_eff_poss_ratio = get_stat.get_opp_eff_pos_ratio(curr[0][0].strip(), opp_eff_poss_ratio)
        team2_opp_eff_poss_ratio = get_stat.get_opp_eff_pos_ratio(curr[0][1], opp_eff_poss_ratio)

        #get teams possesions per game
        team1_poss_per_game = get_stat.get_poss_per_game(curr[0][0].strip(), possesions)
        team2_poss_per_game = get_stat.get_poss_per_game(curr[0][1], possesions)

        #get 3 point %
        team1_three_perc = get_stat.get_three_perc(curr[0][0].strip(), three_perc)
        team2_three_perc = get_stat.get_three_perc(curr[0][1], three_perc)

        # get Opp 3 point %
        team1_opp_3 = get_stat.opp_three(curr[0][0].strip(), opp_three)
        team2_opp_3 = get_stat.opp_three(curr[0][1], opp_three)

        #get % points from 3
        team1_perc_from_3 = get_stat.get_perc_fr_three(curr[0][0].strip(), perc_fr_three)
        team2_perc_from_3 = get_stat.opp_three(curr[0][1],  perc_fr_three)

        # get home rating
        team1_home_rating = get_stat.get_home_rating(curr[0][0].strip(), home_rating)
        team2_home_rating = get_stat.get_home_rating(curr[0][1], home_rating)

        # get away rating
        team1_away_rating = get_stat.get_away_rating(curr[0][0].strip(), away_rating)
        team2_away_rating = get_stat.get_away_rating(curr[0][1], away_rating)

        # get l5 rating
        team1_l5_rating = get_stat.get_l5_rating(curr[0][0].strip(), l5_rating)
        team2_l5_rating = get_stat.get_l5_rating(curr[0][1], l5_rating)



        new_matchup = matchups(team1, team2, team1_rank, team2_rank, team1_ppg, team2_ppg, team1_sos, team2_sos, team1_opp_ppg, team2_opp_ppg, team1_eff_fg_perc, team2_eff_fg_perc,
                           team1_opp_eff_fg_perc, team2_opp_eff_fg_perc, team1_reb_rate, team2_reb_rate, team1_three_perc, team2_three_perc, team1_opp_3, team2_opp_3, team1_perc_from_3, team2_perc_from_3, team1_poss_per_game, team2_poss_per_game,
                           team1_eff_poss_ratio, team2_eff_poss_ratio, team1_opp_eff_poss_ratio, team2_opp_eff_poss_ratio, all_matchups, team1_home_rating, team2_home_rating, team1_away_rating, team2_away_rating, team1_l5_rating, team2_l5_rating)

        all_matchups.append(new_matchup)
        #new_matchup.display_matchup()
        if total > 0:
            total = int(total)
            #print(f"\n{team2} \u2191 {total}")
            dict = {team2,total}
            #print(dict)
        else:
            total = int(abs(total))
            #print(f"\n{team1} \u2191 {total}")
            dict = {team1,total}
        #    print(dict)

        summary.append(dict)

        matchups_list.append(curr)
        #print(link.text)
        next_element = link.find_next_sibling()
        #print("_______________________________________________________")
        #print("\n")
        while next_element and next_element.name != 'a':
            next_element = next_element.find_next_sibling()

for game in all_matchups:
    game.display_matchup()


project_instance = Project(all_matchups)

# Display all matchups
project_instance.display_all_matchups()

# Display projected scores and winners
project_instance.proj_score(False)

# Display accumulated winners and margins
project_instance.display_winners()

