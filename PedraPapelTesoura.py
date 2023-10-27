from tkinter import *

root = Tk();
root.geometry("500x500")

#pontuacao

contagem1=0
contagem2=0
empate=0

#Alterar dinamico o valor da label

d_contagem1 = StringVar()
d_contagem2 = StringVar()
d_empate = StringVar()

#Criação das Label de contagem

lbl_contagemJogador1 = Label(root,text="0", background="green", width=10, height=5, textvariable=d_contagem1).place(x=30,y=20)
lbl_contagemJogador2 = Label(root,text="0", background="green", width=10, height=5, textvariable=d_contagem2).place(x=280,y=20)
lbl_empate = Label(root,text="0", background="red", width=10, height=5, textvariable=d_empate).place(x=150,y=20)

#verifica os valores
def verificarValores():
    if(sb_valores.get() == "pedra" and sb_valores2.get() == "pedra"):
        d_empate.set(empate+1)
        botao()
    elif(sb_valores.get() == "papel" and sb_valores2.get() == "papel"):
        d_empate.set(empate+1)
    elif(sb_valores.get() == "tesoura" and sb_valores2.get() == "tesoura"):
        d_empate.set(empate+1)
        return "SEM VALORES"

#criacao do spinbox

sb_valores = Spinbox(root,values=('pedra','papel','tesoura'))
sb_valores.pack()
sb_valores.place(x=50,y=150)

sb_valores2 = Spinbox(root,values=('pedra','papel','tesoura'))
sb_valores2.pack()
sb_valores2.place(x=50,y=200)

btn_jogar = Button(root,text="Jogar",command=verificarValores)
btn_jogar.pack()
btn_jogar.place(x=50, y=250)

def botao():
    btn_jogar = Button(root,text="Jogar",command=verificarValores)
    return "oi"



#Criacao da Entrada De Valores Para Comparação
#txt_Jogador1 = Entry(root, text="Jogador 1:", background="#dde", foreground="#009", width=30).place(x=50,y=200)
#txt_Jogador2 = Entry(root, text="Jogador 2:", background="#dde", foreground="#009", width=30).place(x=50,y=250)


root.mainloop()



def main():
    botao()

if __name__ == '__main__':
    main()