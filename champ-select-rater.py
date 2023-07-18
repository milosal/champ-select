import sys
import json
from PIL import Image, ImageDraw
from using_lolpedia import lolpedia_to_dict


'''
TODO: 
   1. 
'''

# Access my database of champion damage types
with open("champ-database.json") as file:
        champ_data = json.load(file)

def main():

    while True:
        try:
            # Two ways to enter your draft
            draft_type = input("'Self,' 'Paste,' or 'JSON' draft? ").lower().strip()
        except EOFError:
            sys.exit()
        if draft_type == "self":
            # Get user input for the picks in the draft for both sides
            blue_picks, red_picks = self_draft() 
            break
        elif draft_type == "paste":
            blue_picks, red_picks = paste_draft()
            break
        else: 
            pass

    # Simple sum of the damage types
    bad, bap, bdefense, rad, rap, rdefense = simple_damage_sum(blue_picks, red_picks)

    # Prints the damage profile of each comp
    print(f"Blue side has {bad + bap + bdefense} total stat profile: {bad} ad, {bap} ap, {bad + bap} total damage, and {bdefense} tankiness.")
    print(f"Red side has {rad + rap + rdefense} total stat profile: {rad} ad, {rap} ap, {rad + rap} total damage, and {rdefense} tankiness.")

    # Prints an image of the comps
    print_question = input("Would you like to print an image of the draft? (y/n) ")
    if print_question == "y":
        print_draft(blue_picks, red_picks)

def simple_damage_sum(blue_comp, red_comp):

    blue_ad_total = 0
    red_ad_total = 0

    blue_ap_total = 0
    red_ap_total = 0

    blue_defense_total = 0
    red_defense_total = 0

    for champ in blue_comp:
        blue_ad_total = blue_ad_total + champ_data[champ]["ad"]
        blue_ap_total = blue_ap_total + champ_data[champ]["ap"]
        blue_defense_total = blue_defense_total + champ_data[champ]["defense"]

    for champ in red_comp:
        red_ad_total = red_ad_total + champ_data[champ]["ad"]
        red_ap_total = red_ap_total + champ_data[champ]["ap"]
        red_defense_total = red_defense_total + champ_data[champ]["defense"]
        
    return blue_ad_total, blue_ap_total, blue_defense_total, red_ad_total, red_ap_total, red_defense_total


def print_draft(blue_picks, red_picks):

    blue_images = {}
    red_images = {}

    for champ in blue_picks:
        blue_images[champ] = Image.open(f"/Users/colesalvador/pythonshit/personal/league-stuff/champ-select-project/champion-images/{champ}.png").resize((200, 200))

    for champ in red_picks:
        red_images[champ] = Image.open(f"/Users/colesalvador/pythonshit/personal/league-stuff/champ-select-project/champion-images/{champ}.png").resize((200, 200))

    draft_image = Image.new("RGB", (1650, 1100))

    draft_image.paste(blue_images[blue_picks[0]], (0, 100))
    draft_image.paste(blue_images[blue_picks[1]], (0, 300))
    draft_image.paste(blue_images[blue_picks[2]], (0, 500))
    draft_image.paste(blue_images[blue_picks[3]], (0, 700))
    draft_image.paste(blue_images[blue_picks[4]], (0, 900))

    draft_image.paste(red_images[red_picks[0]], (1450, 100))
    draft_image.paste(red_images[red_picks[1]], (1450, 300))
    draft_image.paste(red_images[red_picks[2]], (1450, 500))
    draft_image.paste(red_images[red_picks[3]], (1450, 700))
    draft_image.paste(red_images[red_picks[4]], (1450, 900))

    draw = ImageDraw.Draw(draft_image)
    draw.rectangle([0, 0, 825, 100], fill=(20, 0, 220))
    draw.rectangle([825, 0, 1650, 100], fill=(200, 0, 20))

    draft_image.show()

def paste_draft():

    lolpedia_data = input("Please paste a match from lolpedia text mode: ")

    dictionary_data = lolpedia_to_dict(lolpedia_data)

    blue_picks = dictionary_data["match_0"]["blue_comp"]
    red_picks = dictionary_data["match_0"]["red_comp"]

    return blue_picks, red_picks


def self_draft():

    blue_picks = []
    red_picks = []

    while True:
        try:
            b1 = input("B1: ")
        except EOFError:
            sys.exit()
        if b1 in champ_data:
             blue_picks.append(b1)
             break
        else:
            pass
    
    while True:
        try:
            r1 = input("R1: ")
        except EOFError:
            sys.exit()
        if r1 in champ_data:
             red_picks.append(r1)
             break
        else:
            pass

    while True:
        try:
            r2 = input("R2: ")
        except EOFError:
            sys.exit()
        if r2 in champ_data:
             red_picks.append(r2)
             break
        else:
            pass    

    while True:
        try:
            b2 = input("B2: ")
        except EOFError:
            sys.exit()
        if b2 in champ_data:
             blue_picks.append(b2)
             break
        else:
            pass

    while True:
        try:
            b3 = input("B3: ")
        except EOFError:
            sys.exit()
        if b3 in champ_data:
             blue_picks.append(b3)
             break
        else:
            pass

    while True:
        try:
            r3 = input("R3: ")
        except EOFError:
            sys.exit()
        if r3 in champ_data:
             red_picks.append(r3)
             break
        else:
            pass

    while True:
        try:
            r4 = input("R4: ")
        except EOFError:
            sys.exit()
        if r4 in champ_data:
             red_picks.append(r4)
             break
        else:
            pass

    while True:
        try:
            b4 = input("B4: ")
        except EOFError:
            sys.exit()
        if b4 in champ_data:
             blue_picks.append(b4)
             break
        else:
            pass
    
    while True:
        try:
            b5 = input("B5: ")
        except EOFError:
            sys.exit()
        if b5 in champ_data:
             blue_picks.append(b5)
             break
        else:
            pass

    while True:
        try:
            r5 = input("R5: ")
        except EOFError:
            sys.exit()
        if r5 in champ_data:
             red_picks.append(r5)
             break
        else:
            pass
    
    return blue_picks, red_picks


if __name__ == "__main__":
    main()