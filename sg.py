import PySimpleGUI as sg
import SwedishWordle  


sg.theme('Reddit')


sz=(40,15)
fs = 'Frankline 20'

col1=[[sg.Text('Ledtråd', font = fs)],[sg.Text( "...", key = "lista", justification = 'center', background_color='blue', size=sz)]]
col2=[[sg.Text('Ord', font = fs)],[sg.Text("...", key = "ord", justification = 'center', background_color='blue', size=sz)]]
col3=[[sg.Text('Antal gissningar', font = fs)],[sg.Text("...", justification = 'center', font = 'Franklin 50', key = "antal", background_color='blue', size = (20,15))]]


layout1 = [
    [sg.Text('Hej och välkomna till vår wordguesser!', font = 'Franklin 26')],
    [sg.Text('Spelet går ut på att du ska försöka gissa vilket ord med fem bokstäver som jag tänker på! \nNär du har gissat på ett ord så kan du se vilket eller vilka bokstäver som finns i det riktiga ordet. \n0 betyder att bokstaven inte finns i ordet\n1 betyder att bokstaven är rätt men på fel plats \n2 betyder att bokstaven är rätt och på rätt plats', font = 'Franklin 17')],
    [sg.Text('Vill du starta ett nytt spel?', font = 'Franklin 20'), sg.Button("Ja, starta nytt spel", font = 'Franklin 20', key="get_new")]
    ]
    
layout2 = [
    [sg.Input(key = 'gissning' , font = 'Franklin 20'), sg.Button('gissa', font = 'Franklin 20', key='gissa')],
    [sg.Column(col1 , element_justification='c'), sg.Column(col2, element_justification='c'), sg.Column(col3, element_justification= 'c')]]

layout3 = [
    [sg.Text('Grattis! du vann!', font = 'Franklin 26') ],
    [sg.Text('Vill du spela igen?', font = 'Franklin 26'), sg.Button('ja!', key = 'kör_igen', font = 'Franklin 26')],
    ]

layout4 = [
    [sg.Text("Felaktig längd på ord. Du gissade \"{word_guess}\". Detta spel är om ord som är {len(self._word)} i längd")]
]

layout = [
    [sg.Column(layout1, key = 'COL1'), sg.Column(layout2, visible = False, key = 'COL2'), sg.Column(layout3, visible = False, key = 'COL3')]]

window = sg.Window("Wordguesser", layout)


layout = 1

tidigare_gissningar = []
tidigare_ord = []
antal_gissningar= 0

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
        antal_gissningar += 1
        window["antal"].update(antal_gissningar)

        if guess == game.Get_current_word():
            window[f'COL{layout}'].update(visible = False)
            layout = layout + 1
            window[f'COL{layout}'].update(visible = True)
    
        
            
  
        
window.close()



