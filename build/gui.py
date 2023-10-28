
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/deborah/Documentos/GitHub/Conversor-de-Moedas/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1303x852")
window.configure(bg = "#474747")


canvas = Canvas(
    window,
    bg = "#474747",
    height = 852,
    width = 1303,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1303.0,
    100.0,
    fill="#1B1B1B",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    233.0,
    47.0,
    image=image_image_1
)

canvas.create_rectangle(
    249.0,
    396.0,
    702.0,
    482.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    36.0,
    310.0,
    anchor="nw",
    text="Digite a moeda de troca:",
    fill="#FFFFFF",
    font=("Roboto Mono", 25 * -1)
)

canvas.create_text(
    36.0,
    229.0,
    anchor="nw",
    text="Digite a moeda inicial:",
    fill="#FFFFFF",
    font=("Roboto Mono", 25 * -1)
)

canvas.create_text(
    36.0,
    143.0,
    anchor="nw",
    text="Digite o valor:",
    fill="#FFFFFF",
    font=("Roboto Mono", 25 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1004.0,
    472.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1006.0,
    504.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1142.0,
    422.0,
    image=image_image_4
)

canvas.create_text(
    1038.0,
    408.0,
    anchor="nw",
    text="MÍNIMO",
    fill="#979090",
    font=("Roboto Mono", 15 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    871.0,
    422.0,
    image=image_image_5
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    910.0,
    424.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=847.0,
    y=411.0,
    width=126.0,
    height=24.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1185.0,
    424.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1122.0,
    y=411.0,
    width=126.0,
    height=24.0
)

canvas.create_text(
    765.0,
    409.0,
    anchor="nw",
    text="MÁXIMO",
    fill="#979090",
    font=("Roboto Mono", 15 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1004.0,
    157.0,
    image=image_image_6
)

canvas.create_text(
    814.0,
    143.0,
    anchor="nw",
    text="Cotações Atualizadas:",
    fill="#4E4E4E",
    font=("Roboto Mono", 30 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    946.0,
    257.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    489.0,
    157.0,
    image=image_image_8
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    432.5,
    155.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=316.0,
    y=142.0,
    width=233.0,
    height=24.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    527.5,
    237.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=411.0,
    y=224.0,
    width=233.0,
    height=24.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    544.5,
    314.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=428.0,
    y=301.0,
    width=233.0,
    height=24.0
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    556.0,
    315.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    549.0,
    237.0,
    image=image_image_10
)

canvas.create_text(
    779.0,
    248.0,
    anchor="nw",
    text="Digite a moeda:",
    fill="#414040",
    font=("Roboto Mono", 20 * -1)
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    871.0,
    340.0,
    image=image_image_11
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    910.0,
    340.0,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=847.0,
    y=327.0,
    width=126.0,
    height=24.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    1051.5,
    504.0,
    image=entry_image_7
)
entry_7 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=865.0,
    y=491.0,
    width=373.0,
    height=24.0
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    1142.0,
    340.0,
    image=image_image_12
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    1185.0,
    340.0,
    image=entry_image_8
)
entry_8 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=1122.0,
    y=327.0,
    width=126.0,
    height=24.0
)

canvas.create_text(
    1038.0,
    325.0,
    anchor="nw",
    text="VENDA",
    fill="#979090",
    font=("Roboto Mono", 15 * -1)
)

canvas.create_text(
    769.0,
    325.0,
    anchor="nw",
    text="COMPRA",
    fill="#979090",
    font=("Roboto Mono", 15 * -1)
)

canvas.create_text(
    769.0,
    491.0,
    anchor="nw",
    text="VARIAÇÃO",
    fill="#979090",
    font=("Roboto Mono", 15 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    475.0,
    436.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=257.0,
    y=422.0,
    width=436.0,
    height=27.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    1048.0,
    260.0,
    image=entry_image_10
)
entry_10 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=974.0,
    y=250.0,
    width=148.0,
    height=18.0
)

canvas.create_rectangle(
    551.0,
    22.0,
    1276.0,
    73.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    556.0,
    39.0,
    anchor="nw",
    text="Obs: Atualmente, só está disponível a conversão de Dólar para real.",
    fill="#7A7272",
    font=("Roboto Mono", 18 * -1)
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    369.0,
    682.0,
    image=image_image_13
)

canvas.create_text(
    51.0,
    554.0,
    anchor="nw",
    text="Moedas disponíveis para troca:\n[USD] Dólar Americano\n[CAD] Dólar Canadense\n[AUD] Dólar Australiano\n[EUR] Euro\n[GBP] Libra Esterlina\n[JPY] Iene\n[BTC] BitCoin\n ",
    fill="#000000",
    font=("Roboto Mono", 25 * -1)
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    483.0,
    49.0,
    image=image_image_14
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1151.0,
    y=229.0,
    width=108.0,
    height=56.0
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    1205.0,
    257.0,
    image=image_image_15
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
    x=1151.0,
    y=229.0,
    width=108.0,
    height=56.0
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
    x=37.0,
    y=394.0,
    width=196.0,
    height=90.0
)
window.resizable(False, False)
window.mainloop()
