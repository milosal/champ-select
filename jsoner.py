import json
import os

with open('champ-data.json') as file:
    champ_data = json.load(file)

just_data = champ_data["data"]

relevant_champ_data = {}

for champ in just_data:
    champ = champ
    relevant_champ_data[champ] = {
        "ad": just_data[champ]["info"]["attack"],
        "ap": just_data[champ]["info"]["magic"],
        "defense": just_data[champ]["info"]["defense"]
    }

with open("champ-database.json", "w") as file:
    json.dump(relevant_champ_data, file, indent=4)
