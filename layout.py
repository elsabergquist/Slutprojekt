
import PySimpleGUI as sg


class Gui:
    def design_startsida(ds):      

        
        layout = [
            [sg.Text('Hej och välkomna till Wordle!', font = 'Franklin 26', justification = 'center')],
            [sg.Text('Spelet går ut på att du ska försöka gissa vilket ord med fem bokstäver som jag tänker på! \nNär du har gissat på ett ord så kan du se vilket eller vilka bokstäver som finns i det riktiga ordet. \n0 betyder att bokstaven inte finns i ordet\n1 betyder att bokstaven är rätt men på fel plats \n2 betyder att bokstaven är rätt och på rätt plats', font = 'Franklin 17', justification = 'center')],
            [sg.Text('Vill du starta ett nytt spel?', font = 'Franklin 20', justification = 'center'), 
            sg.Button('Ja, starta nytt spel', font = 'Franklin 20', key='starta_spel_button'), 
            sg.Button('Highscore', font = 'Franklin 20', key='highscore_button')]
            ]    

        window = sg.Window('Window Title', layout)    

        window.close()
        
    
    
   
