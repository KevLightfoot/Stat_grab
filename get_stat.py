import requests
from bs4 import BeautifulSoup
import re
import codecs


#Basketball State 7-231
def get_sos(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    #rank_element = element.find_previous_sibling(class_='rank tr_arrow')
    rank_element = element.find_previous_sibling(class_=lambda value: value and value.startswith('rank tr_arrow'))
    rank = rank_element.get_text()
    #print(rank.strip())
    return rank

def get_bb_ppg(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    if stat.strip() != "--":
        stat_value = float(stat.strip())
    else:
        stat_value = float(0.0)
    #print(stat.strip(), end='')
    #print(f" ({rank.strip()})")

    return stat_value, int(rank.strip())

def get_opp_ppg(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    if stat.strip() != "--":
        stat_value = float(stat.strip())
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_eff_fg_perc(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat_with_percent = stat_element.get_text()
    rank = rank_element.get_text()
    # Remove the '%' character and convert to float
    if stat_with_percent.strip() != "--":
        stat_value = float(stat_with_percent.replace('%', '').strip())
    else:
        stat_value = float(0.0)
    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_opp_eff_fg_perc(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat_with_percent = stat_element.get_text()
    rank = rank_element.get_text()
    # Remove the '%' character and convert to float
    if stat_with_percent.strip() != "--":
        stat_value = float(stat_with_percent.replace('%', '').strip())
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_reb_margin(team,que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat_with_percent = stat_element.get_text()
    rank = rank_element.get_text()
    # Remove the '%' character and convert to float
    if stat_with_percent.strip() != "--":
        stat_value = float(stat_with_percent.replace('%', '').strip())
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_poss_per_game(team,que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    if stat.strip() != "--":
        stat_value = float(stat.strip())
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_eff_pos_ratio(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    if stat.strip() != "--":
        stat_value = float(stat.strip())
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_opp_eff_pos_ratio(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    if stat.strip() != "--":
        stat_value = float(stat.strip())
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_three_perc(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_cleaned = stat.replace('%', '').strip()
    if stat_cleaned.strip() != "--":
        stat_value = float(stat_cleaned)
    else:
        stat_value = float(0.0)
    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def opp_three(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_cleaned = stat.replace('%', '').strip()
    if stat_cleaned.strip() != "--":
        stat_value = float(stat_cleaned)
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_perc_fr_three(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_cleaned = stat.replace('%', '').strip()
    if stat_cleaned.strip() != "--":
        stat_value = float(stat_cleaned)
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_home_rating(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_=lambda value: value and value.startswith('rank tr_arrow'))
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    if stat.strip() != "--":
        stat_value = float(stat.strip())
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_away_rating(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_=lambda value: value and value.startswith('rank tr_arrow'))
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    if stat.strip() != "--":
        stat_value = float(stat.strip())
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())

def get_l5_rating(team, que):
    # Find the element with class "text-left nowrap" and data-sort attribute "Miss Val St"
    element = que.find(class_='nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_=lambda value: value and value.startswith('rank tr_arrow'))
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    if stat.strip() != "--":
        stat_value = float(stat.strip())
    else:
        stat_value = float(0.0)    # print(stat.strip(), end='')
    # print(f" ({rank.strip()})")
    return stat_value, int(rank.strip())












#New implementation

def get_fb_ppg(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})

    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate

    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')

    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate

    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')

    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate

    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())

    return stat_value, int(rank.strip())

def get_ranking(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r', encoding='windows-1252') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='nowrap', attrs={'data-sort': team})
    if element:
        # Find the preceding sibling element with class "rank text-center"
        rank_element = element.find_previous_sibling(class_=lambda value: value and value.startswith('rank tr_arrow'))
        # Extract the rank from the rank_element
        rank = rank_element.get_text(strip=True) if rank_element else "N/A"
        return int(rank)  # Return the ranking as an integer
    raise ValueError(f"Team '{team}' not found in the file.")

def get_fb_oppg(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())

def get_ypg(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())

def get_oypg(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())

def get_pyd(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())

def get_opyd(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())

def get_sacks_all(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())

def get_sacks(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())

def get_ryd(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())

def get_oryd(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())

def get_third_down(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())

def get_opp_third_down(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())

def get_redzone(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())

def get_redzone_d(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())

def get_fb_sos(team, file_path):
    # Read the HTML content from the specified file
    with codecs.open(file_path, 'r') as file:
        html_content = file.read()
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the element with class "text-left nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='text-left nowrap', attrs={'data-sort': team})
    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())
'''
def get_rtd(team, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    que = BeautifulSoup(html_content, 'html.parser')
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})

    if element is None:
        raise ValueError(f"Team '{team}' not found in the file.")

    rank_element = element.find_previous_sibling(class_='rank text-center')
    stat_element = element.find_next_sibling(class_='text-right')
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())
    






# Football Stats
def get_ranking(team, soup):
    # Find the element with class "nowrap" and data-sort attribute matching the team name
    element = soup.find(class_='nowrap', attrs={'data-sort': team})

    if element:
        # Find the preceding sibling element with class "rank text-center"
        rank_element = element.find_previous_sibling(class_=lambda value: value and value.startswith('rank tr_arrow'))

        # Extract the rank from the rank_element
        rank = rank_element.get_text(strip=True) if rank_element else "N/A"
        return int(rank)  # Return the ranking as an integer

    # Return None or a default value if the team is not found
    return None
def get_fb_ppg(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})

    if element is None:
        return (0.0, 0)  # Or any default values you deem appropriate

    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')

    # Check if rank_element is found
    if rank_element is None:
        print(f"Skipping {team}: Rank element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate

    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')

    # Check if stat_element is found
    if stat_element is None:
        print(f"Skipping {team}: Stat element not found.")
        return (0.0, 0)  # Or any default values you deem appropriate

    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())

    return stat_value, int(rank.strip())

def get_fb_oppg(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())




#Start of implementation
def get_ypg(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())




def get_oypg(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())
def get_fb_sos(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())
def get_pyd(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())
def get_opyd(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())
def get_sacks_all(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())
def get_sacks(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())
def get_ryd(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())
def get_rtd(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())
def get_oryd(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())
def get_third_down(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())
def get_opp_third_down(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())

def get_hadv(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())

def get_arat(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat_value = float(stat.strip())
    return stat_value, int(rank.strip())
def get_redzone(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())
def get_redzone_d(team, que):
    element = que.find(class_='text-left nowrap', attrs={'data-sort': team})
    # Find the preceding sibling element with class "rank text-center"
    rank_element = element.find_previous_sibling(class_='rank text-center')
    # Find the next sibling element with class "text-right"
    stat_element = element.find_next_sibling(class_='text-right')
    # Extract the rank from the element
    stat = stat_element.get_text()
    rank = rank_element.get_text()
    stat = stat.replace('%', '')
    stat_value = float(stat.strip())
    stat_value = round(stat_value, 2)
    return stat_value, int(rank.strip())



'''
def calculate(team1, team2, team1_sos, team2_sos):
    diff = team1_sos - team2_sos
    if diff > 0:
        return diff
    else:
        return diff