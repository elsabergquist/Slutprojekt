import json
import os
import os.path

highscore_file_path = "highscore.json"
#Highscore funktion

def uppdate_highscorelist(guess, antal_gissningar):
    highscore = read_highscorelist()
    high_score_element = {"word":guess,"count":antal_gissningar}
    highscore.append(high_score_element)
    with open(highscore_file_path, "w") as f:
        json.dump(highscore, f)

    return highscore 

def read_highscorelist():
    if os.path.isfile(highscore_file_path):
        with open(highscore_file_path, "r") as file:
            highscore = json.load(file)

        return highscore
    else:
        empty_highscore = []
        with open(highscore_file_path, "w") as f:
            json.dump(empty_highscore, f)

        return empty_highscore

