import requests
import customtkinter as ctk
from PIL import Image, ImageTk

win = ctk.CTk()
win.title('MatVoker 0.1 Beta')
win.geometry('600x500')

site = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
deckid = ''

rubashkaimg = 'C:/projects/matVoker/rubashka.jpg'

rubashkaimg = Image.open(rubashkaimg)
rubashkaimg = ctk.CTkImage(light_image=rubashkaimg, size=(70, 90))

compcard = []

playercard = {}

mast = {'ACE': '14', 'KING': '13', 'QUEEN': '12', 'JACK': '11'}

def newcolodafunc():
    global deckid
    deckid = requests.get(site).json()['deck_id']
    

newcolodafunc()

def newcardfunc(x):
    site = f"https://deckofcardsapi.com/api/deck/{deckid}/draw/?count={str(x)}"
    card = requests.get(site).json()
    for i in range(x):
        cardimg = card['cards'][i]['image']
        cardvalue = card['cards'][i]['value']
        if not cardvalue.isnumeric():
            cardvalue = mast.get(cardvalue)
        if x == 3:
            compcard.append({'img': cardimg, 'value': cardvalue})
        else:
            playercard.update({'img': cardimg, 'value': cardvalue})
    
    

newcardfunc(3)
newcardfunc(1)
print(compcard, playercard)

def compcardimgfunc(numcard):
    cardimgsite = requests.get(compcard[numcard]['img'], stream=True).raw
    cardimgsite = Image.open(cardimgsite)
    cardimgsite = ctk.CTkImage(light_image=cardimgsite, size=(70, 90))
    if numcard == 0:
        cardbot1.configure(image=cardimgsite, text='', state='disabled', fg_color='grey')
    elif numcard == 1:
        cardbot2.configure(image=cardimgsite, text='', state='disabled', fg_color='grey')
    elif numcard == 2:
        cardbot3.configure(image=cardimgsite, text='', state='disabled', fg_color='grey')

def playercardimgfunc():
    cardimgsite = requests.get(playercard['img'], stream=True).raw
    cardimgsite = Image.open(cardimgsite)
    cardimgsite = ctk.CTkImage(light_image=cardimgsite, size=(70, 90))
    cardplayerlabel.configure(image=cardimgsite, text='')
    
    
def checkfunc(x):
    if cardmoreval.get() == 'none':
        print('Error')
    else:
        if cardmoreval.get() == 'Больше':
            print('more', x)
            if int(playercard['value']) > int(compcard[x]['value']):
                print('Win')
            else:
                print('lose')
        elif cardmoreval.get() == 'Меньше':
            print('less', x)
            if int(playercard['value']) < int(compcard[x]['value']):
                print('Win')
            else:
                print('lose')
        elif cardmoreval.get() == 'Равно':
            print('equally', x)
            if int(playercard['value']) == int(compcard[x]['value']):
                print('Win')
            else:
                print('lose')
        
        playercard.update({'img': compcard[x]['img'], 'value': compcard[x]['value']})
        playercardimgfunc()
        compcardimgfunc(x)

def rubashkafunc():
    cardbot1.configure(image=rubashkaimg, text='')
    cardbot2.configure(image=rubashkaimg, text='')
    cardbot3.configure(image=rubashkaimg, text='')


frameinfo = ctk.CTkFrame(win)
framecards = ctk.CTkFrame(win)

frameinfo.pack(pady=10, padx=20)
framecards.pack(pady=10, padx=20)


cardbot1 = ctk.CTkButton(framecards, text='', width=80, command=lambda: checkfunc(0))
cardbot2 = ctk.CTkButton(framecards, text='', width=80, command=lambda: checkfunc(1))
cardbot3 = ctk.CTkButton(framecards, text='', width=80, command=lambda: checkfunc(2))

cardmoreval = ctk.StringVar(value='none')
cardmore = ctk.CTkSegmentedButton(framecards, values=['Больше', 'Равно', 'Меньше'], variable=cardmoreval)
cardmorelabel = ctk.CTkLabel(framecards, text='Ваша карта:')

cardplayerlabel = ctk.CTkLabel(framecards, text='')

cardbot1.grid(row=0, column=0, pady=10, padx=10)
cardbot2.grid(row=0, column=1, pady=10, padx=10)
cardbot3.grid(row=0, column=2, pady=10, padx=10)

cardmorelabel.grid(row=1, column=1)
cardmore.grid(row=2, column=1, pady=10)

cardplayerlabel.grid(row=3, column=1, pady=20, padx=10)

cardpoints = ctk.CTkLabel(frameinfo, text=f'Очки: ')
cardbet = ctk.CTkLabel(frameinfo, text=f'Ставка: ')

cardbet.pack()
cardpoints.pack()

playercardimgfunc()

rubashkafunc()


win.mainloop()
