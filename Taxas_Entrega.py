import pandas as pd
from tkinter import *
import tkinter.font as tkFont

def buscar():
    quant = 0
    error = 0
    c = 0
    x = str(entry.get()).lower().strip()
    if len(x) <= 2:
        texto1['text'] = 'Endereço não encontrado!'
        entry.delete(0, END)
        return
    for item in db['Endereço']:
        item = item.lower().strip()
        taxa = db['Taxa de entrega'][c]
        if x in item:
            quant += 1
            error = 1
            texto1['text'] = 'A taxa de entrega no {} é R${:.2f}'.format(item, taxa)
        elif error == 0:
            texto1['text'] = 'Endereço não encontrado!'
        elif quant > 1:
            texto1['text'] = f'Existem {quant} endereços com "{x}"!'
        c += 1
    entry.delete(0, END)


db = pd.read_excel("Taxas de entrega.xlsx", engine='openpyxl')

root = Tk()
root.title('Taxas')
root.geometry('500x250')
root.resizable(False, False)

background = '#696969'
background2 = '#D3D3D3'

root.configure(bg=background)
fontStyle = tkFont.Font(family="Comic Sans MS", size=13)

entry = Entry(root, bd='5', bg=background2)
entry.pack(padx=10, pady=10)

botao = Button(root, text='Buscar', bd='5', command=buscar, height=2, width=10, bg=background2)
botao.pack(padx=10, pady=10)

texto1 = Label(root, text='', font=fontStyle, bg=background, foreground='white')
texto1.pack()


root.mainloop()

