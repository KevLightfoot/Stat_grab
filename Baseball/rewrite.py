# Open the file in read mode
with open('C:\krl1901\Stat_Grab v2.0\Rankings.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

# Replace "St." with "State" in the content
modified_content = content.replace("ST.", "STATE")
modified_content = modified_content.replace("MISSISSIPPI", "OLE MISS")

with open('C:\\krl1901\\Stat_Grab v2.0\\Rankings.txt', 'w') as file:
    # Write the modified content back to the file
    file.write(modified_content)

# Open the file in read mode
with open('C:\krl1901\Stat_Grab v2.0\Rankings.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

modified_content = modified_content.replace("SOUTH CAROLINA UPSTATE", "USC UPSTATE")
modified_content = modified_content.replace("PURDUE FT. WAYNE","PURDUE FORT WAYNE")
modified_content = modified_content.replace("ALABAMA BIRMINGHAM","UAB")
modified_content = modified_content.replace("STATE JOHN'S","ST. JOHN'S")
modified_content = modified_content.replace("MARYLAND BALTIMORE COUNTY","UMBC")
modified_content = modified_content.replace("TEXAS SAN ANTONIO","UTSA")
modified_content = modified_content.replace("TENNESSEE MARTIN ","TENNESSEE-MARTIN")
modified_content = modified_content.replace("CENTRAL FLORIDA","UCF")
modified_content = modified_content.replace("SAINT JOSEPH'S","Saint JOSEPH’S")
modified_content = modified_content.replace("STATE LOUIS","SAINT LOUIS")
modified_content = modified_content.replace("QUEENS NC","QUEENS (NC)")
modified_content = modified_content.replace("CITADEL","THE CITADEL")
modified_content = modified_content.replace("SOUTHERN CAL","SOUTHERN CALIFORNIA")
modified_content = modified_content.replace("CALIFORNIA RIVERSIDE","UC RIVERSIDE")
modified_content = modified_content.replace("CALIFORNIA DAVIS","UC DAVIS")
modified_content = modified_content.replace("CAL STATE BAKERSFIELD","CSU BAKERSFIELD")
modified_content = modified_content.replace("NORTH CAROLINA GREENSBORO","UNC GREENSBORO")
modified_content = modified_content.replace("MIAMI OHIO","MIAMI (OH)")
modified_content = modified_content.replace("ILLINOUS CHICAGO","ILLINOIS-CHICAGO")
modified_content = modified_content.replace("NEVADA LAS VEGAS","UNLV")
modified_content = modified_content.replace("SE MISSOURI STATE","SOUTHEAST MISSOURI STATE")
modified_content = modified_content.replace("OLE MISS STATE","MISSISSIPPI STATE")
modified_content = modified_content.replace("SE LOUISIANA","SOUTHEASTERN LOUISIANA")
modified_content = modified_content.replace("SOUTHERN OLE MISS","SOUTHERN MISS")
modified_content = modified_content.replace("LOUISIANA-MONROE","UL MONROE")
modified_content = modified_content.replace("STATE PETER'S","SAINT PETER’S")
modified_content = modified_content.replace("OLE MISS VALLEY STATE","MISSISSIPPI VALLEY STATE")
modified_content = modified_content.replace("NORTH CAROLINA STATE","NC STATE")
modified_content = modified_content.replace("TEXAS ARLINGTON  ","UT ARLINGTON")
modified_content = modified_content.replace("TEXAS RIO GRANDE VALLEY","UT RIO GRANDE VALLEY")
modified_content = modified_content.replace("S. F. AUSTIN","STEPHEN F. AUSTIN")
modified_content = modified_content.replace("NORTH CAROLINA WILMINGTON","UNC WILMINGTON")
modified_content = modified_content.replace("NICHOLLS STATE","NICHOLLS")
modified_content = modified_content.replace("SAM HOUSTON STATE","SAM HOUSTON")
modified_content = modified_content.replace("MIAMI FLORIDA","MIAMI")
modified_content = modified_content.replace("McNEESE STATE","MCNEESE ")
modified_content = modified_content.replace("OAKLAND MI","OAKLAND")
modified_content = modified_content.replace("LOUISIANA-LAFAYETTE","LOUISIANA")
modified_content = modified_content.replace("TROY STATE","TROY")
modified_content = modified_content.replace("MT. STATE MARY'S MD.","MOUNT ST. MARY’S")
modified_content = modified_content.replace("STATE BONAVENTURE","ST. BONAVENTURE")
modified_content = modified_content.replace("PRESBYTERIAN COLLEGE","PRESBYTERIAN")
modified_content = modified_content.replace("STATE JOSEPH'S PA.","SAINT JOSEPH’S")
modified_content = modified_content.replace("MOUNT ST. MARY�S ","SAINT MARY�S")
modified_content = modified_content.replace("STATE THOMAS MN","ST. THOMAS")
modified_content = modified_content.replace("MARYLAND EASTERN SHORE","UMES")
modified_content = modified_content.replace("CAL BAPTIST","CALIFORNIA BAPTIST")
modified_content = modified_content.replace("MASS-LOWELL ","UMASS LOWELL")
modified_content = modified_content.replace("ST. JOHN'S","ST. JOHN’S")
modified_content = modified_content.replace("NORTH CAROLINA ASHEVILLE","UNC ASHEVILLE")
modified_content = modified_content.replace("CALIFORNIA SAN DIEGO","UC SAN DIEGO")
modified_content = modified_content.replace("CALIFORNIA IRVINE","UC IRVINE")
modified_content = modified_content.replace("CALIFORNIA SANTA BARBARA","UC SANTA BARBARA")
modified_content = modified_content.replace("STATE MARY'S CA.","SAINT MARY’S")
modified_content = modified_content.replace("TOWSON STATE","TOWSON")
modified_content = modified_content.replace("WISCONSIN MILWAUKEE","MILWAUKEE")
modified_content = modified_content.replace("OHIO UNIVERSITY ","OHIO")
modified_content = modified_content.replace("LONG ISLAND UNIVERSITY","LONG ISLAND")
modified_content = modified_content.replace("ARKANSAS LITTLE ROCK","LITTLE ROCK")
modified_content = modified_content.replace("CENTRAL CONNECTICUT STATE","CENTRAL CONNECTICUT")
modified_content = modified_content.replace("NORTH CAROLINA CHARLOTTE","CHARLOTTE")
modified_content = modified_content.replace("GRAMBLING STATE","GRAMBLING")
modified_content = modified_content.replace("UTAH VALLEY STATE","UTAH VALLEY")
modified_content = modified_content.replace("NEBRASKA OMAHA","OMAHA")
modified_content = modified_content.replace("MONMOUTH NJ","MONMOUTH ")
modified_content = modified_content.replace("MIDDLE TENNESSEE STATE","MIDDLE TENNESSEE")
























with open('C:\\krl1901\\Stat_Grab v2.0\\Rankings.txt', 'w') as file:
    # Write the modified content back to the file
    file.write(modified_content)