from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label

import random

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Administrator\Documents\GitHub\Tarot_Day\Tarot_Day\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Card:
    def __init__(self, name, location):
        self.name = name
        self.location = location

#card location
c1 = Card('THE COMPUTER', 'image_8.png')
c2 = Card('THE FLOWER', 'image_9.png')
c3 = Card('THE SOUP', 'image_10.png')
c4 = Card('THE GUITAR', 'image_11.png')
c5 = Card('THE TROPHY', 'image_12.png')
c6 = Card('THE KNIFE', 'image_13.png')
c7 = Card('THE MIC', 'image_14.png')
c8 = Card('THE CAMERA', 'image_15.png')
c9 = Card('THE GLASSES', 'image_16.png')
c10 = Card('THE BALL', 'image_17.png')
c11 = Card('THE MONEY', 'image_18.png')
c12 = Card('THE PLANT', 'image_19.png')
c13 = Card('THE BOOK', 'image_20.png')
c14 = Card('THE CALENDER', 'image_21.png')
c15 = Card('THE GLASS', 'image_22.png')

list_card = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15]

def random_card():
    card1 = random.choice(list_card)
    card2 = random.choice(list_card)
    card3 = random.choice(list_card)
    while card1==card2 or card1==card3 or card2==card3:
        card1 = random.choice(list_card)
        card2 = random.choice(list_card)
    return card1, card2, card3

card_tuple = random_card()

window = Tk()

window.geometry("1200x853")
window.configure(bg = "#FFFFFF")
window.update()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 853,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=random_card,
    relief="flat"
)
button_1.place(
    x=492.0,
    y=657.0,
    width=217.0,
    height=91.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    273.0,
    386.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    599.0,
    386.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    925.0,
    386.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    272.5,
    599.5,
    image=entry_image_1
)
entry_1 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    anchor='center',
    text=card_tuple[0].name,
    font=("Prompt Regular", 25 * -1)
)
entry_1.place(
    x=151.0,
    y=578.0,
    width=243.0,
    height=41.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    598.5,
    599.5,
    image=entry_image_2
)
entry_2 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    anchor='center',
    text=card_tuple[1].name,
    font=("Prompt Regular", 25 * -1)
)
entry_2.place(
    x=477.0,
    y=578.0,
    width=243.0,
    height=41.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    924.5,
    599.5,
    image=entry_image_3
)
entry_3 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    anchor='center',
    text=card_tuple[2].name,
    font=("Prompt Regular", 25 * -1)
)
entry_3.place(
    x=803.0,
    y=578.0,
    width=243.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=732.0,
    y=670.0,
    width=67.0,
    height=60.10296630859375
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=405.0,
    y=672.0,
    width=58.0,
    height=55.0
)

canvas.create_text(
    420.0, #x
    82.0, #y
    anchor="nw",
    text="Tarot Day !",
    fill="#000000",
    font=("Prompt Bold", 70 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    600.0,
    10.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1190.0,
    426.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    9.0,
    426.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    601.0,
    843.0,
    image=image_image_7
)
#photo card
image_image_8 = PhotoImage(
    file=relative_to_assets(card_tuple[0].location))
image_8 = canvas.create_image(
    274.0,
    387.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets(card_tuple[1].location))
image_9 = canvas.create_image(
    605.0,
    386.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets(card_tuple[2].location))
image_10 = canvas.create_image(
    925.0,
    386.0,
    image=image_image_10
)

window.resizable(False, False)
window.mainloop()