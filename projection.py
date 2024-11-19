from bs4 import BeautifulSoup

# Open and read the saved HTML file
with open('projections.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the rows of the table that contain the desired data
table_rows = soup.find_all('tr')

# Print the header row with cleaner formatting, including 'Ret Mins' and shifting other labels
print(
    f"{'Rk':<4} {'Team':<20} {'AdjOE':<15} {'AdjDE':<15} {'Ret Mins':<10} {'RPMs':<10} {'Talent':<10} {'Exp.':<10} {'Trans.':<10}")

# Iterate through each row and extract the relevant data
for row in table_rows:
    # Extract all <td> elements in the row
    columns = row.find_all('td')

    if len(columns) >= 12:  # Ensure the row has enough columns
        # Extract the data
        rank = columns[0].get_text(strip=True)
        team = columns[1].get_text(strip=True)
        conference = columns[2].get_text(strip=True)

        # Get AdjOE and AdjDE values, and their respective national ranks
        adj_oe = columns[3].get_text(strip=True).split('<br')[0]
        adj_de = columns[4].get_text(strip=True).split('<br')[0]
        adj_oe_rank = columns[3].find_all('span')[0].get_text(strip=True)  # National rank for AdjOE
        adj_de_rank = columns[4].find_all('span')[0].get_text(strip=True)  # National rank for AdjDE

        # Format the AdjOE and AdjDE with the rank
        adj_oe_formatted = f"{float(adj_oe):.1f} --> {adj_oe_rank}"
        adj_de_formatted = f"{float(adj_de):.1f} --> {adj_de_rank}"

        # Extract Ret Mins and Ret Poss Mins
        ret_mins = columns[8].get_text(strip=True)  # Ret Mins
        rpm = columns[9].get_text(strip=True)      # RPMs

        # Extract the remaining fields (Talent, Exp., Trans.)
        talent = columns[10].get_text(strip=True)
        exp = columns[11].get_text(strip=True)
        trans = columns[12].get_text(strip=True)

        # Print the formatted data with proper column alignment
        print(
            f"{rank:<4} {team:<20} {adj_oe_formatted:<15} {adj_de_formatted:<15} {ret_mins:<10} {rpm:<10} {talent:<10} {exp:<10} {trans:<10}")

'''import requests

# URL to fetch
url = "https://www.barttorvik.com/trankpre.php"

try:
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP request errors

    # Save the HTML content to a file
    with open("projections.txt", "w", encoding='utf-8') as file:
        file.write(response.text)

    print("HTML content saved to projections.txt successfully.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
'''