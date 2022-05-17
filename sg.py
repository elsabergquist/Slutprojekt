from ast import Dict
from email.mime import application
import PySimpleGUI as sg
import SwedishWordle  
from highscorelista import *
from layout import *

#listor
highscore_file_path = 'highscore.json'
highscore = []
antal_gissningar = 0
highscore_gissningar = []
highscore_ord = []

    
layout = all_layout()
window = sg.Window('Wordle', layout, size=(800,400))
layout = 1


while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    if event == 'kör_igen_button' or event == 'kör_igen2_button':
        
        window[f'COL{layout}'].update(visible = False)
        layout = 1
        window[f'COL{layout}'].update(visible = True)

    if event == 'starta_spel_button':
        tidigare_gissningar = []
        tidigare_ord = []
        antal_gissningar= 0

        #funktion av window och upppdatering av layout
        
        window[f'COL{layout}'].update(visible = False)
        layout = layout + 1
        window[f'COL{layout}'].update(visible = True)
        window['lista'].update('')
        window['lista'].update(visible = True)
        window['ord'].update('')
        window['antal'].update('')
        game = SwedishWordle.Game(5)
        window.Refresh()

    if event == 'tillbaka_button':
        window[f'COL{layout}'].update(visible = False)
        layout = 1
        window[f'COL{layout}'].update(visible = True)


    if event == 'highscore_button':
        # laddar highscore
        highscore = read_highscorelist()
        highscore.sort(key=lambda x: x["count"])
        
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

        layout = 1
        window[f'COL{layout}'].update(visible = False)
        layout= layout + 4
        window[f'COL{layout}'].update(visible = True)
      

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
                window[f'COL{layout}'].update(visible = False)
                layout = layout + 2
                window[f'COL{layout}'].update(visible = True)

            if guess == game.Get_current_word():

                window[f'COL{layout}'].update(visible = False)
                layout = layout + 1
                window[f'COL{layout}'].update(visible = True)
                highscore = uppdate_highscorelist(guess, antal_gissningar)
                

        except ValueError:
            felmeddelande = 'Någonting gick fel'
            window['varning'].update(felmeddelande)

    
window.close()



