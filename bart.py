from bs4 import BeautifulSoup

# Read the HTML content from bart.txt
with open('bart.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize a list to store extracted data
teams_data = []

# Iterate through each row in the table
for row in soup.find_all('tr', class_='seedrow'):
    # Extracting the Rank
    rank = row.find('td', class_='lowrowclick').text.strip()

    # Extracting the Team Name
    team_name = row.find('td', class_='teamname').text.strip()

    # Extracting AdjOE and its rank
    adjoe_td = row.find('td', class_='1')
    adjoe = adjoe_td.text.split("<br/>")[0].strip()
    adjoe_rank = adjoe_td.find('span', class_='lowrow').text.strip()

    # Extracting AdjDE and its rank
    adjde_td = row.find('td', class_='2')
    adjde = adjde_td.text.split("<br/>")[0].strip()
    adjde_rank = adjde_td.find('span', class_='lowrow').text.strip()

    # Extracting EFG% and its rank
    efg_td = row.find('td', class_='7')
    efg = efg_td.text.split("<br/>")[0].strip()
    efg_rank = efg_td.find('span', class_='lowrow').text.strip()

    # Extracting EFGD% and its rank
    efgd_td = row.find('td', class_='8')
    efgd = efgd_td.text.split("<br/>")[0].strip()
    efgd_rank = efgd_td.find('span', class_='lowrow').text.strip()

    # Extracting TOR and its rank
    tor_td = row.find('td', class_='11')
    tor = tor_td.text.split("<br/>")[0].strip()
    tor_rank = tor_td.find('span', class_='lowrow').text.strip()

    # Extracting TORD and its rank
    tord_td = row.find('td', class_='12')
    tord = tord_td.text.split("<br/>")[0].strip()
    tord_rank = tord_td.find('span', class_='lowrow').text.strip()

    # Extracting ORB and its rank
    orb_td = row.find('td', class_='13')
    orb = orb_td.text.split("<br/>")[0].strip()
    orb_rank = orb_td.find('span', class_='lowrow').text.strip()

    # Extracting DRB and its rank
    drb_td = row.find('td', class_='14')
    drb = drb_td.text.split("<br/>")[0].strip()
    drb_rank = drb_td.find('span', class_='lowrow').text.strip()

    # Append to list
    teams_data.append({
        'Rank': rank,
        'Team': team_name,
        'AdjOE': (adjoe, adjoe_rank),
        'AdjDE': (adjde, adjde_rank),
        'EFG%': (efg, efg_rank),
        'EFGD%': (efgd, efgd_rank),
        'TOR': (tor, tor_rank),
        'TORD': (tord, tord_rank),
        'ORB': (orb, orb_rank),
        'DRB': (drb, drb_rank)
    })

# Print extracted data in formatted columns
print(f"{'Rk':<4} {'Team':<20} {'AdjOE (Rank)':<15} {'AdjDE (Rank)':<15} {'EFG% (Rank)':<15} {'EFGD% (Rank)':<15} {'TOR (Rank)':<15} {'TORD (Rank)':<15} {'ORB (Rank)':<15} {'DRB (Rank)':<15}")
for team in teams_data:
    print(f"{team['Rank']:<4} {team['Team']:<20} "
          f"{team['AdjOE'][0]} ({team['AdjOE'][1]})".ljust(15) + " "
          f"{team['AdjDE'][0]} ({team['AdjDE'][1]})".ljust(15) + " "
          f"{team['EFG%'][0]} ({team['EFG%'][1]})".ljust(15) + " "
          f"{team['EFGD%'][0]} ({team['EFGD%'][1]})".ljust(15) + " "
          f"{team['TOR'][0]} ({team['TOR'][1]})".ljust(15) + " "
          f"{team['TORD'][0]} ({team['TORD'][1]})".ljust(15) + " "
          f"{team['ORB'][0]} ({team['ORB'][1]})".ljust(15) + " "
          f"{team['DRB'][0]} ({team['DRB'][1]})")
