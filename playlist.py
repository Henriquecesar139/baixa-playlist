#importações
from pytube import YouTube, Playlist #youtube
from os import system, name #Descobrir S.O e executar arquivo secundário
from tkinter import * #interface gráfica

#função que baixa a playlist
def download():
    system(f'{exec} aviso.py BAiXANDO...')    
    try:
        pl = playl.get()
        nome = nomepl.get()
        playlist = Playlist(pl)
        for url in playlist:
            yt = YouTube(url)
            audio = yt.streams.filter(only_audio = True)[0]
            audio.download(output_path = nome)
        system(f'{exec} aviso.py PLaylist Baixada')  
    except:
         system(f'{exec} aviso.py Ocorreu Algum Erro')  

#tela
tela = Tk()
tela.title('Baixador de Playlist')
tela.resizable(False, False)
tela.geometry('580x500')
tela['bg'] = 'red'

#usado para compatibilidade entre Windows e Linux
if name == 'nt':
    exec = 'python'
else:
    exec = 'python3'

#título no topo da tela
titulo = Label(tela, text = 'Baixador De PlayList\n\n', font = 'Arial 20', fg = 'white', bg = 'red')
titulo.pack(side = TOP)

#mensagem
msg = Label(tela, text = 'Link Da Playlist', font = 'Arial', fg = 'white', bg = 'red')
msg.pack(side = TOP)

#Entry que recebe o link da playlist
playl = Entry(tela, width = 60)
playl.pack(side = TOP)

#segunda mensagem
msg2 = Label(tela, text = '\n\nNome Da playlist', fg = 'white', font = 'arial', bg = 'red')
msg2.pack(side = TOP)

#Entry que recebe a pasta de destino
nomepl = Entry(tela, width = 60)
nomepl.pack(side = TOP)

#botão que chama a função de baixar
baixar = Button(tela, text = 'Baixar', width = 30, fg = 'white', bg = 'black', command = download)
baixar.pack(side = BOTTOM)

tela.mainloop()