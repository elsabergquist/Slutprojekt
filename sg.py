import PySimpleGUI as sg
import SwedishWordle  


sg.theme('Reddit')


sz=(20,30)
fs = 'Frankline 20'
tc= 'white'

col1=[[sg.Text('Ledtråd', font = fs)],
[sg.Text( "...", key = "lista", text_color = tc, justification = 'center', font = 'Franklin 20', background_color='blue', size=sz)]]
col2=[[sg.Text('Ord', font = fs)],
[sg.Text("...", key = "ord", text_color = tc, justification = 'center', font = 'Franklin 20', background_color='blue', size=sz)]]
col3=[[sg.Text('Antal gissningar', font = fs)],
[sg.Text("...",  key = "antal", text_color = tc, justification = 'center', font = 'Franklin 50', background_color='blue', size = (20,15))]]


layout1 = [
    [sg.Text('Hej och välkomna till vår wordguesser!', font = 'Franklin 26')],
    [sg.Text('Spelet går ut på att du ska försöka gissa vilket ord med fem bokstäver som jag tänker på! \nNär du har gissat på ett ord så kan du se vilket eller vilka bokstäver som finns i det riktiga ordet. \n0 betyder att bokstaven inte finns i ordet\n1 betyder att bokstaven är rätt men på fel plats \n2 betyder att bokstaven är rätt och på rätt plats', font = 'Franklin 17')],
    [sg.Text('Vill du starta ett nytt spel?', font = 'Franklin 20'), sg.Button("Ja, starta nytt spel", font = 'Franklin 20', key="get_new")]
    ]
    
layout2 = [
    [sg.Input(key = 'gissning' , font = 'Franklin 20'), sg.Button('gissa', font = 'Franklin 20', key='gissa')],
    [sg.Text("", key= "varning", font = fs)]
    [sg.Column(col1 , element_justification='c'), sg.Column(col2, element_justification='c'), sg.Column(col3, element_justification= 'c')]]

layout3 = [
    [sg.Text('Grattis! du vann!', font = 'Franklin 26') ],
    [sg.Text('Vill du spela igen?', font = 'Franklin 26'), sg.Button('ja!', key = 'kör_igen', font = 'Franklin 26')],
    ]

layout4 = [
    [sg.Text('Du har max 5 gissningar', font = fs)],   [sg.Text('Vill du spela igen?', font = 'Franklin 26'), sg.Button('ja!', key ="kör_igen2", font = 'Franklin 26')],
    ]

layout = [
    [sg.Column(layout1, key = 'COL1'), sg.Column(layout2, visible = False, key = 'COL2'), sg.Column(layout3, visible = False, key = 'COL3'), sg.Column(layout4, visible = False, key = 'COL4')]]

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

    if event == "kör_igen" or event == "kör_igen2":
        window[f'COL{layout}'].update(visible = False)
        layout = 1
        window[f'COL{layout}'].update(visible = True)

    if event == "get_new":
        window[f'COL{layout}'].update(visible = False)
        layout = layout + 1
        window[f'COL{layout}'].update(visible = True)
        window["lista"].update("")
        window["lista"].update(visible = True)
        # tidigare_ord
        window["ord"].update("")
        window["antal"].update("")
        game = SwedishWordle.Game(5)
        window.Refresh()

    
    if event == "gissa":
        guess = values['gissning']#hämta från inputen
        
        try:
            new_guess = game.Guess(guess)
        except ValueError:
            print("gick fel")
            window
            break

        message = f'{new_guess}'
        tidigare_gissningar.append(message)
        tidigare_ord.append(guess)
        window["lista"].update("\n".join(tidigare_gissningar))
        # tidigare_ord
        window["ord"].update("\n".join(tidigare_ord))
        antal_gissningar += 1
        window["antal"].update(antal_gissningar)
      
        if antal_gissningar >= 5: 
            antal_gissningar = 0
            window[f'COL{layout}'].update(visible = False)
            layout = layout + 2
            window[f'COL{layout}'].update(visible = True)

        if guess == game.Get_current_word():
            window[f'COL{layout}'].update(visible = False)
            layout = layout + 1
            window[f'COL{layout}'].update(visible = True)




window.close()



