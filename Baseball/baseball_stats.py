def find_rank(team_name):
    with open('C:\\krl1901\\Stat_Grab v2.0\\Rankings.txt', 'r') as file:
        for line in file:
            # Split the line by whitespace
            parts = line.split()

            # Extracting the team name which may contain multiple words
            file_team_name = ' '.join(parts[1:-4])

            # Check if the provided team name is contained within the line's team name
            if team_name.lower() in file_team_name.lower():
                return int(parts[0]), float(parts[-1])

        # If the team is not found, return None
        return [0,1]

def find_record(team_name):
    # Read the text file
    with open("C:\\krl1901\\Stat_Grab v2.0\\Rankings.txt", "r") as file:
        lines = file.readlines()

    # Iterate through each line
    for line in lines:
        # Split the line into parts
        parts = line.split()

        # Extract the team name
        team_name_parts = []
        for part in parts[1:]:
            if part.isdigit():
                break
            team_name_parts.append(part)

        # Combine team name parts into a single string
        current_team_name = " ".join(team_name_parts)

        # Check if the current line contains the team name (case insensitive)
        if current_team_name.lower() == team_name.lower():
            # Extract the record (first 2 digits after the team name)
            record = "-".join(parts[-5:-3])
            # Return the record
            return record

    # If the team name is not found, return None
    return None


