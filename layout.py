import PySimpleGUI as sg

def design():
    sg.theme('Reddit')
    sz=(20,30) #size
    fs = 'Frankline 20' #fontsize
    tc= 'white' #text color
    return sz,fs,tc


def layout_all():
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
    col4=[[sg.Text('Vinstgissning:', font = fs)],[sg.Text('...', key = 'rätt_ord', text_color = tc, justification = 'center', font = fs, background_color='blue', size = (15,20))]]
    col5=[[sg.Text('Antal gissningar', font = fs)],[sg.Text('...', key = 'score', text_color = tc, justification = 'center', font = fs, background_color='blue', size = (15,20))]]

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
    [sg.Text('Highscore', font = fs), sg.Button('Tillbaka till startsidan', key ='tillbaka_button', font= 'Frankline 20' )],
    [sg.Column(col4, element_justification=('c')), sg.Column(col5, element_justification=('c'))]
        ]
            
    return layout_startsida,layout_spelsida,layout_vinstsida,layout_maxgissningar,layout_highscorelista
    
    
   
