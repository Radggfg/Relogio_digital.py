from tkinter import * 
import tkinter
from datetime import datetime
import pyglet
import os

# Verifica se o arquivo de fonte existe
font_file = "digital-7.ttf"
if os.path.exists(font_file):
    pyglet.font.add_file(font_file)
else:
    print(f"Arquivo de fonte '{font_file} não encontrado. Certifique-se de que o arquivo está no diretório correto.")

############# cores ###############
cor1 = "#3d3d3d" # preta
cor2 = "#fafcff" # branca
cor3 = "21c25c"  # verde
cor4 = "#eb463b" # vermelha
cor5 = "#dedcdc" # cinza
cor6 = "#3080f0" # azul

fundo = cor1
cor = cor4

janela  =Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

def relogio():

    tempo=datetime.now()

    hora=tempo.strftime("%H:%M:%S")
    dia_semana=tempo.strftime("%A")
    dia=tempo.day
    mes=tempo.strftime("%B")
    ano=tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + "  " + str(dia) + 
            "/" + str(mes) + "/" + str(ano))



l1=Label(janela, text="", font=("digtal-7 80"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)


l2=Label(janela, text="", font=("digtal-7 17"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)



relogio()
janela.mainloop()