import json

# This function gets the winrate of a champion in one or all regions from the data I have hard-loading into regional/results

def main():

    games_played, winrate = get_winrate_one_region()
    print(f"{games_played} games played with a {winrate}% winrate")




def get_winrate_one_region():

    champion = input("Which champion would you like to get the winrate of? ")
    region = input("In which region? ").lower()
    split = input("In Summer or Spring? ").lower()

    with open(f"/league-stuff/champ-select-project/regional-results/{region.lower()}_2023_{split.lower()}.json") as file:
        region_data = json.load(file)

    wins = 0
    losses = 0

    for match in region_data:
        if champion in region_data[match]["blue_comp"]:
            if region_data[match]["winner"] == "B":
                wins += 1
            else:
                losses += 1
        elif champion in region_data[match]["red_comp"]:
            if region_data[match]["winner"] == "R":
                wins += 1
            else: 
                losses += 1
    
    games_played = wins + losses
    if games_played == 0:
        winrate = "N/A"
    else:
        winrate = round((wins / games_played) * 100, 2)

    return games_played, winrate




if __name__ == "__main__":
    main()
