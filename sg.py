import PySimpleGUI as sg
import SwedishWordle  


sg.theme('DarkTeal6')

layout1 = [
    [sg.Text('Hej och välkomna till vår wordguesser!, Spelet går ut på att du ska försöka gissa vilket ord med fem bokstäver som jag tänker på! Vill du starta ett nytt spel?'), sg.Button("ja, starta nytt spel", key="get_new")],
    [sg.Text('När du har gissat på ett ord så kan du se vilket eller vilka bokstäver som finns i det riktiga ordet. 0 betyder att bokstaven inte finns i ordet, 1 betyder att bokstaven är rätt men på fel plats, 2 betyder att bokstaven är rätt och på rätt plats')]]
    
layout2 = [
    [sg.Input(key = 'gissning'), sg.Button('gissa', key='gissa')],
    [sg.Text("...", key = "lista")]
    ]

layout3 = [
    [sg.Input(), sg.Button('gissa', key='gissa2')],
]
layout4 = [
    [sg.Input(), sg.Button('gissa', key='gissa3')],
]

layout = [
    [sg.Column(layout1, key = 'COL1'), sg.Column(layout2, visible = False, key = 'COL2'), sg.Column(layout3, visible = False, key = 'COL3')]
]

window = sg.Window("Wordguesser", layout)

layout = 1

tidigare_gissningar = []

while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    if event == "get_new":
        window[f'COL{layout}'].update(visible = False)
        layout = layout + 1 
        window[f'COL{layout}'].update(visible = True)
        game = SwedishWordle.Game(5)
    
    if event == "gissa":
        guess = values['gissning']#hämta från inputen
        new_guess = game.Guess(guess)
        message = f'{new_guess}'
        tidigare_gissningar.append(message+'\n')
        window["lista"].update(tidigare_gissningar)
        
    def lasbart(tidigare_gissningar):

    text = ""
    for tuppel in tidigare_gissningar:
        for s in tuppel:
            text+=str(s)+ " "
        text += "\n"
    return text
    
    
    # if event == "gissa2":
        #guess2 = game.Guess('gissa')
        #message = f'{guess2}'
        #layout = layout + 1 
        #window[f'COL{layout}'].update(visible = True)
        #window["info"].update(message)

    #if event == "gissa3":
        #guess3 = game.Guess('gissa')
        #message = f'{guess3}'
        #window["info"].update(message)
        

   # if guess == result:
    #    correct = True
    #    break

    #if correct:
    #    sg.popup('You win!')

    



window.close()


#window[f'COL{layout}'].update(visible = False) layout = layout + 1 if layout < 3 else 1 window[f'COL{layout}'].update(visible = True)