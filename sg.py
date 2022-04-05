import PySimpleGUI as sg
from SwedishWordle import *


layout = [
    [sg.Text('Hej och välkomna till vår wordguesser!, Vill du starta ett nytt spel?'), sg.Button("ja, starta nytt spel", key="get_new")],
    [sg.Text("...", key="info")]]

window = sg.Window("Wordguesser", layout)

while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    if event == "get_new":
        response = Start_new_game(self, word_length = 5)
        message = f'{response}'
        window["gissning"].update(visible = False)
        window["info"].update(message)
    
    if event == "gissning":
        response = Guess(self, word_guess)
        message = f'{response}'
        window["info"].update(message)


window.close()
