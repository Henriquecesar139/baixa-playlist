from tkinter import *
from sys import argv

tela = Tk()
tela.geometry('300x200')
tela.resizable(False, False)
tela['bg'] = 'red'

aviso1 = Label (tela, text = ' '.join(argv[1::]) + '\n\n\n', fg = 'white', bg = 'red', font = 'arial 20')
aviso1.pack(side = TOP)

aviso2 = Label (tela, text = 'Você pode fechar esse aviso', fg = 'white', bg = 'red', font = 'arial 15')
aviso2.pack(side = TOP)

tela.mainloop()