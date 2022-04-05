import PySimpleGUI as sg
from exampleusage import *


layout = [
    [sg.Text('Hej och välkomna till vår wordguesser!, Spelet går ut på att du ska försöka gissa vilket ord med fem bokstäver som jag tänker på! Vill du starta ett nytt spel?'), sg.Button("ja, starta nytt spel", key="get_new")],
    [sg.Text('När du har gissat på ett ord så kan du se vilket eller vilka bokstäver som finns i det riktiga ordet. 0 betyder att bokstaven inte finns i ordet, 1 betyder att bokstaven är rätt men på fel plats, 2 betyder att bokstaven är rätt och på rätt plats')],
    [sg.Input(), sg.Button('gissa', key='gissa')],
    [sg.Text("...", key="info")]]

window = sg.Window("Wordguesser", layout)

while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    if event == "get_new":
        game = SwedishWordle.Game(5)
        message = f'{game}'
        window["gissning"].update(visible = False)
        window["info"].update(message)
    
    if event == "gissa":
        guess1 = game.Guess(input)
        message = f'{guess1}'
        window["info"].update(message)


window.close()
