from ast import Dict
from email.mime import application
import PySimpleGUI as sg
import SwedishWordle  
import io
import highscorelista
import json
import os.path

#Design
sg.theme('Reddit')
sz=(20,30) #size
fs = 'Frankline 20' #fontsize
tc= 'white' #text color

#kolummner
col1=[[sg.Text('Ledtråd', font = fs)],
[sg.Text( '...', key = 'lista', text_color = tc, justification = 'center', font = 'Franklin 20', background_color='blue', size=sz)]]
col2=[[sg.Text('Ord', font = fs)],
[sg.Text('...', key ='ord', text_color = tc, justification = 'center', font = 'Franklin 20', background_color='blue', size=sz)]]
col3=[[sg.Text('Antal gissningar', font = fs)],
[sg.Text('...',  key = 'antal', text_color = tc, justification = 'center', font = 'Franklin 50', background_color='blue', size = (20,5))]]
col4=[[sg.Text("...", key = 'score', text_color = tc, justification = 'center', font = 'Franklin 50', background_color='blue', size = (15,10))]]

#layout
layout_startsida = [
    [sg.Text('Hej och välkomna till Wordle!', font = 'Franklin 26', justification = 'center')],
    [sg.Text('Spelet går ut på att du ska försöka gissa vilket ord med fem bokstäver som jag tänker på! \nNär du har gissat på ett ord så kan du se vilket eller vilka bokstäver som finns i det riktiga ordet. \n0 betyder att bokstaven inte finns i ordet\n1 betyder att bokstaven är rätt men på fel plats \n2 betyder att bokstaven är rätt och på rätt plats', font = 'Franklin 17', justification = 'center')],
    [sg.Text('Vill du starta ett nytt spel?', font = 'Franklin 20', justification = 'center'), 
    sg.Button('Ja, starta nytt spel', font = 'Franklin 20', key='starta_spel_button'), 
    sg.Button('Highscore', font = 'Franklin 20', key='highscore_button')]
    ]
    
layout_spelsida = [
    [sg.Input(key = 'gissning' , font = 'Franklin 20'), 
    sg.Button('gissa', font = 'Franklin 20', key='gissa_button')],
    [sg.Text("...", key= 'varning', font = fs)],
    [sg.Column(col1 , element_justification='c'), 
    sg.Column(col2, element_justification='c'), 
    sg.Column(col3, element_justification= 'c')]
    ]

layout_vinstsida = [
    [sg.Text('Grattis! du vann!', font = 'Franklin 26') ],
    [sg.Text('Vill du spela igen?', font = 'Franklin 26'), 
    sg.Button('Ja!', key ='kör_igen_button', font = 'Franklin 26')],
    ]

layout_maxgissningar = [
    [sg.Text('Du har max 5 gissningar', font = fs)],   
    [sg.Text('Vill du spela igen?', font = 'Franklin 26'), 
    sg.Button('Ja!', key ='kör_igen2_button', font = 'Franklin 26')],
    ]

layout_highscorelista = [
    [sg.Text('Highscore', font = fs)], 
    [sg.Column(col4, element_justification=('c')), 
    sg.Button('Tillbaka till startsidan', key ='tillbaka_button', font= 'Frankline 20' )]]

layout = [
    [sg.Column(layout_startsida, key = 'COL1'), sg.Column(layout_spelsida, visible = False, key = 'COL2'), sg.Column(layout_vinstsida, visible = False, key = 'COL3'), sg.Column(layout_maxgissningar, visible = False, key = 'COL4'),  sg.Column(layout_highscorelista, visible = False, key = 'COL5')]]

window = sg.Window('Wordle', layout, size=(800,300) )

layout = 1

#listor
highscore_file_path = 'highscore.json'
highscore = []

#Öppnar highscore filen
if os.path.isfile(highscore_file_path) :

    f = open(highscore_file_path, 'r')
    #Reading from file
    highscore = json.load(f)
    f.close()

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
        window[f'COL{layout}'].update(visible = False)
        layout = layout + 1
        window[f'COL{layout}'].update(visible = True)
        window['lista'].update('')
        window['lista'].update(visible = True)
        # tidigare_ord
        window['ord'].update('')
        window['antal'].update('')
        game = SwedishWordle.Game(5)
        window.Refresh()

    if event == 'tillbaka_button':
        window[f'COL{layout}'].update(visible = False)
        layout = 1
        window[f'COL{layout}'].update(visible = True)


    if event == 'highscore_button':
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
                print(highscore)
                highscore = highscorelista.uppdate_highscorelist(highscore, guess, antal_gissningar)
                window['antal'].update(antal_gissningar)
                window['score'].update(highscore)

                #adderar nytt highscore till listan
                with open(highscore_file_path, 'w') as f:
                    json.dump(highscore, f)
         

        except ValueError:
            felmeddelande = 'Någonting gick fel'
            window['varning'].update(felmeddelande)

    
window.close()



