
import PySimpleGUI as sg
import SwedishWordle  
from highscorelista import *
from layout import *

   
layout = all_layout()
window = sg.Window('Wordle', layout, size=(800,400))
layout = 1


def update_window(layout, window, n):
    if n == 1:
        window[f'COL{layout}'].update(visible = False)
        layout = 1
        window[f'COL{layout}'].update(visible = True)
    if n== 2:
        window[f'COL{layout}'].update(visible = False)
        layout = layout + 1
        window[f'COL{layout}'].update(visible = True)
    if n == 3:
        window[f'COL{layout}'].update(visible = False)
        layout = layout + 2
        window[f'COL{layout}'].update(visible = True)
    if n ==4:
        window[f'COL{layout}'].update(visible = False)
        layout= layout + 4
        window[f'COL{layout}'].update(visible = True)

    return layout

while True:
    event, values = window.read()

    highscore = []

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    if event == 'kör_igen_button' or event == 'kör_igen2_button':
        layout = update_window(layout, window,1)

    if event == 'starta_spel_button':
        tidigare_gissningar = []
        tidigare_ord = []
        antal_gissningar= 0
        #funktion av window och upppdatering av layout
        layout = update_window(layout, window, 2)

        window['lista'].update('')
        window['lista'].update(visible = True)
        window['ord'].update('')
        window['antal'].update('')

        game = SwedishWordle.Game(5)
        window.Refresh()

    if event == 'tillbaka_button':
        layout = update_window(layout, window, 1)

    if event == 'highscore_button':
        # laddar highscore
        highscore_file_path = 'highscore.json'
        highscore = read_highscorelist()
        highscore_gissningar = []
        highscore_ord = []
        for hs in highscore:
            all_ord = ""
            all_ord += hs["word"]
            highscore_ord.append(all_ord)
                
        window['rätt_ord'].update('\n'.join(highscore_ord[0:9]))

        for hc in highscore:
                
            highest_count = 0
            highest_count += hc['count']
            highscore_gissningar.append(str(highest_count))
 
        window['score'].update(('\n'.join(highscore_gissningar[0:9])))
        layout = update_window(layout, window, 4)
      
    if event == 'gissa_button':
        guess = values['gissning']#hämta från inputen

        try:
            new_guess = game.Guess(guess)
            message = f'{new_guess}'
            tidigare_gissningar.append(message)
            tidigare_ord.append(guess)
            window['lista'].update('\n'.join(tidigare_gissningar))
            # tidigare_ord
            window['ord'].update('\n'.join(tidigare_ord))
            antal_gissningar += 1
            window['antal'].update(antal_gissningar)
        
            if antal_gissningar > 5: 
                antal_gissningar = 0
                tidigare_gissningar = []
                tidigare_ord = []
                layout = update_window(layout, window, 3)

            if guess == game.Get_current_word():
                layout = update_window(layout, window, 2)
                highscore = uppdate_highscorelist(guess, antal_gissningar)
                
        except ValueError:
            felmeddelande = 'Någonting gick fel'
            window['varning'].update(felmeddelande)

window.close()



