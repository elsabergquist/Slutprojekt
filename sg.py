import PySimpleGUI as sg
import SwedishWordle  


sg.theme('DarkTeal6')


sz=(70,70)
col1=[[sg.Text( "...", key = "lista",background_color='Teal', size=sz)]]
col2=[[sg.Text("...", key = "ord", background_color='Teal', size=sz),]]
col3=[[sg.Text("...", key = "ord", background_color='Teal', size=sz),]]


layout1 = [
    [sg.Text('Hej och välkomna till vår wordguesser!, Vill du starta ett nytt spel?'), sg.Button("ja, starta nytt spel", key="get_new")],
    [sg.Text('Spelet går ut på att du ska försöka gissa vilket ord med fem bokstäver som jag tänker på!\nNär du har gissat på ett ord så kan du se vilket eller vilka bokstäver som finns i det riktiga ordet.\n0 betyder att bokstaven inte finns i ordet, 1 betyder att bokstaven är rätt men på fel plats, 2 betyder att bokstaven är rätt och på rätt plats')]]
    
layout2 = [
    [sg.Input(key = 'gissning'), sg.Button('gissa', key='gissa')],
    [sg.Column(col1, element_justification='c'), sg.Column(col2, element_justification='c')]]

layout3 = [
    [sg.Text('Grattis! du vann!')],
    [sg.Text('Vill du spela igen?'), sg.Button('ja!', key = 'kör_igen')],
    [sg.Column(col3, element_justification='c')]]

layout = [
    [sg.Column(layout1, key = 'COL1'), sg.Column(layout2, visible = False, key = 'COL2'), sg.Column(layout3, visible = False, key = 'COL3')]]

window = sg.Window("Wordguesser", layout, size = (1200,300))


layout = 1

tidigare_gissningar = []
tidigare_ord = []


while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    if event == "kör_igen":
        window[f'COL{layout}'].update(visible = False)
        layout = 1
        window[f'COL{layout}'].update(visible = True)

    if event == "get_new":
        window["lista"].update("")
        # tidigare_ord
        window["ord"].update("")
        window[f'COL{layout}'].update(visible = False)
        layout = layout +1
        window[f'COL{layout}'].update(visible = True)
        game = SwedishWordle.Game(5)

    
    if event == "gissa":
        guess = values['gissning']#hämta från inputen
        new_guess = game.Guess(guess)
        message = f'{new_guess}'
        tidigare_gissningar.append(message)
        tidigare_ord.append(guess)
        window["lista"].update("\n".join(tidigare_gissningar))
        # tidigare_ord
        window["ord"].update("\n".join(tidigare_ord))

        if guess == game.Get_current_word():
            window[f'COL{layout}'].update(visible = False)
            layout = layout + 1
            window[f'COL{layout}'].update(visible = True)
            
  
        
window.close()



