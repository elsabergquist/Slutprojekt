import PySimpleGUI as sg
from SwedishWordle import *

layout = [
    [sg.Text('Hej och välkomna till vår wordguesser!, Hur många bokstäver vill du att ordet ska bestå av?'), sg.InputText(key="bokstaver")],
    [sg.Button("gissa", key="gissing")],
    [sg.Text("...", key="info")]]

window = sg.Window("Wordguesser", layout)

while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break


window.close()
