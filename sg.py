import PySimpleGUI as sg
import SwedishWordle  


sg.theme('DarkTeal6')

sz=(70,70)
col1=[[sg.Text("...", key = "lista",background_color='Teal', size=sz)]]
col2=[[sg.Text("...", key = "ord", background_color='Teal', size=sz),]]


layout1 = [
    [sg.Text('Hej och välkomna till vår wordguesser!, Spelet går ut på att du ska försöka gissa vilket ord med fem bokstäver som jag tänker på! Vill du starta ett nytt spel?'), sg.Button("ja, starta nytt spel", key="get_new")],
    [sg.Text('När du har gissat på ett ord så kan du se vilket eller vilka bokstäver som finns i det riktiga ordet. 0 betyder att bokstaven inte finns i ordet, 1 betyder att bokstaven är rätt men på fel plats, 2 betyder att bokstaven är rätt och på rätt plats')]]
    
layout2 = [
    [sg.Input(key = 'gissning'), sg.Button('gissa', key='gissa')],
    [sg.Column(col1, element_justification='c'), sg.Column(col2, element_justification='c')]]

layout = [
    [sg.Column(layout1, key = 'COL1'), sg.Column(layout2, visible = False, key = 'COL2')]]

window = sg.Window("Wordguesser", layout, size = (1000, 500))

layout = 1

tidigare_gissningar = []
tidigare_ord = []


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
        tidigare_gissningar.append(message)
        tidigare_ord.append(guess)
        window["lista"].update(tidigare_gissningar)
        window["ord"].update(tidigare_ord)
        
    def lasbart(tidigare_gissningar):

    text1 = ""

    for tuppel in tidigare_gissningar:
        for s in tuppel:
            text1+=str(s)+ " "
        text1 += "\n"
    return text1
    

window.close()
