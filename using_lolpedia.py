import json
import csv

def main():

    games_to_convert = input("Which file would you like to convert? ")

    with open(f"/Users/colesalvador/pythonshit/personal/league-stuff/champ-select-project/regional-results/{games_to_convert}") as file:
        reader = csv.reader(file) 

        lolpedia_to_dict(reader)

def lolpedia_to_dict(matches):



    dictionaried_results = {}

    i = 0

    for row in matches:
        dictionaried_results[f"match_{i}"] = {"winner": "", "blue_comp": "", "red_comp": ""}

        all_picks = []

        for element in row:
            element = element.replace("\t", " ")
            element = element.split(" ")
            if "" in element:
                element.remove("")
            all_picks.append(element)
            
        if "1" in row[0]:
            dictionaried_results[f"match_{i}"]["winner"] = "B"
        elif "2" in row[0]:
            dictionaried_results[f"match_{i}"]["winner"] = "R"
        else:
            print("No winner found")

        blue_comp = []
        red_comp = []

        blue_comp.append(all_picks[0][1])
        blue_comp.append(all_picks[1][1])
        blue_comp.append(all_picks[2][0])
        blue_comp.append(all_picks[2][3])
        blue_comp.append(all_picks[3][0])

        red_comp.append(all_picks[0][2])
        red_comp.append(all_picks[1][0])
        red_comp.append(all_picks[2][1])
        red_comp.append(all_picks[2][2])
        red_comp.append(all_picks[3][1])


        dictionaried_results[f"match_{i}"]["blue_comp"] = blue_comp

        dictionaried_results[f"match_{i}"]["red_comp"] = red_comp
            
        i += 1
        
    
    file_name = input("File name: ")
    
    
    with open(f"/Users/colesalvador/pythonshit/personal/league-stuff/champ-select-project/regional-results/{file_name}.json", "w") as file:
        json.dump(dictionaried_results, file, indent=4)
    
    
    # return dictionaried_results

if __name__ == "__main__":
    main()