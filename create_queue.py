import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
#basketball s
def sos():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/ranking/schedule-strength-by-other'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    #initialize and populate Queue
    sos = Queue()
    sos.put(soup.prettify())
    sos = BeautifulSoup(sos.get(), 'html.parser')
    return sos
def bb_ppg():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/points-per-game'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    # initialize and populate Queue
    ppg = Queue()
    ppg.put(soup.prettify())
    ppg = BeautifulSoup(ppg.get(), 'html.parser')
    return ppg
def opp_ppg():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    # initialize and populate Queue
    opp_ppg = Queue()
    opp_ppg.put(soup.prettify())
    opp_ppg = BeautifulSoup(opp_ppg.get(), 'html.parser')
    return opp_ppg
def eff_fg_perc():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/effective-field-goal-pct'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    # initialize and populate Queue
    eff_fg_perc = Queue()
    eff_fg_perc.put(soup.prettify())
    eff_fg_perc = BeautifulSoup(eff_fg_perc.get(), 'html.parser')
    return eff_fg_perc
def opp_eff_fg_perc():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/opponent-effective-field-goal-pct'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    opp_eff_fg_perc = Queue()
    opp_eff_fg_perc.put(soup.prettify())
    opp_eff_fg_perc = BeautifulSoup(opp_eff_fg_perc.get(), 'html.parser')
    return opp_eff_fg_perc
def rebound_perc():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/total-rebounding-percentage'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    rebound_perc = Queue()
    rebound_perc.put(soup.prettify())
    rebound_perc = BeautifulSoup(rebound_perc.get(), 'html.parser')
    return rebound_perc
def possesions():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/possessions-per-game'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    possesions = Queue()
    possesions.put(soup.prettify())
    possesions = BeautifulSoup(possesions.get(), 'html.parser')
    return possesions
def eff_poss_ratio():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/effective-possession-ratio'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    eff_poss_ratio = Queue()
    eff_poss_ratio.put(soup.prettify())
    eff_poss_ratio = BeautifulSoup(eff_poss_ratio.get(), 'html.parser')
    return eff_poss_ratio
def opp_eff_poss_ratio():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/opponent-effective-possession-ratio'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    opp_eff_poss_ratio = Queue()
    opp_eff_poss_ratio.put(soup.prettify())
    opp_eff_poss_ratio = BeautifulSoup(opp_eff_poss_ratio.get(), 'html.parser')
    return opp_eff_poss_ratio
def three_perc():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/three-point-pct'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    three_perc = Queue()
    three_perc.put(soup.prettify())
    three_perc = BeautifulSoup(three_perc.get(), 'html.parser')
    return three_perc
def perc_fr_three():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/percent-of-points-from-3-pointers'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    perc_fr_three = Queue()
    perc_fr_three.put(soup.prettify())
    perc_fr_three = BeautifulSoup(perc_fr_three.get(), 'html.parser')
    return perc_fr_three
def opp_three():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/stat/opponent-three-point-pct'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    opp_three = Queue()
    opp_three.put(soup.prettify())
    opp_three = BeautifulSoup(opp_three.get(), 'html.parser')
    return opp_three
def home_rating():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/ranking/home-by-other'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    home_rating = Queue()
    home_rating.put(soup.prettify())
    home_rating = BeautifulSoup(home_rating.get(), 'html.parser')
    return home_rating
def away_rating():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/ranking/away-by-other'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    away_rating = Queue()
    away_rating.put(soup.prettify())
    away_rating = BeautifulSoup(away_rating.get(), 'html.parser')
    return away_rating
def l5_rating():
    # URL of the webpage containing the matchups
    url = 'https://www.teamrankings.com/ncaa-basketball/ranking/last-5-games-by-other'
    # Make a request to the webpage
    html_content = requests.get(url).text
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(html_content, 'html.parser')
    l5_rating = Queue()
    l5_rating.put(soup.prettify())
    l5_rating = BeautifulSoup(l5_rating.get(), 'html.parser')
    return l5_rating

# Function to get HTML content with retry logic
def get_html_with_retry(url, max_retries=5):
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** attempt)
    raise ConnectionError(f"Failed to retrieve data after {max_retries} attempts")




























# Football queues
def ranking():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/ranking/predictive-by-other'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def fb_ppg():
    # URL of the webpage containing points per game
    url = 'https://www.teamrankings.com/college-football/stat/points-per-game'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def fb_oppg():
    # URL of the webpage containing points per game
    url = 'https://www.teamrankings.com/college-football/stat/opponent-points-per-game'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def ypg():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/yards-per-game'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def oypg():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/opponent-yards-per-game'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def fb_sos():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/ranking/season-sos-by-other'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def pyd():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/passing-yards-per-game'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def opyd():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/opponent-passing-yards-per-game'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
    '''
def ptd():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/player-stat/passing-touchdowns'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup'''
def sacks_all():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/qb-sacked-pct'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def sacks():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/sack-pct'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def ryd():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/rushing-yards-per-game'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def oryd():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/opponent-rushing-yards-per-game'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def third_down():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/third-down-conversion-pct'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def opp_third_down():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/opponent-third-down-conversion-pct'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def hadv():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/ranking/home-by-other'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def arat():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/ranking/away-by-other'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def redzone():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/red-zone-scoring-pct'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def redzone_d():
    # URL of the webpage containing the rankings
    url = 'https://www.teamrankings.com/college-football/stat/opponent-red-zone-scoring-pct'
    html_content = get_html_with_retry(url)  # Use the new function to get HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

