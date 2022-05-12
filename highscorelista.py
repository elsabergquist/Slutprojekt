

def uppdate_highscorelist(highscore, guess, antal_gissningar):
    high_score_element = {"word":guess,"count":antal_gissningar}
    highscore.append(high_score_element)
    return(highscore)
