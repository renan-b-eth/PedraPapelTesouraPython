from tkinter import *

root = Tk();
root.geometry("500x500")

#pontuacao
contagem1=0
contagem2=0


#Criação das Label de contagem
lbl_contagemJogador1 = Label(root,text=contagem1, background="green", width=10, height=5).place(x=30,y=20)
lbl_contagemJogador2 = Label(root,text=contagem2, background="green", width=10, height=5).place(x=280,y=20)
lbl_empate = Label(root,text="EMPATE", background="red", width=10, height=5).place(x=150,y=20)


def verificarValores():
    print("Valor: " + str(sb_valores.get()))

#criacao do spinbox

sb_valores = Spinbox(root,values=('pedra','papel','tesoura'))
sb_valores.pack()

btn_jogar = Button(root,text="Jogar")


#Criacao da Entrada De Valores Para Comparação
#txt_Jogador1 = Entry(root, text="Jogador 1:", background="#dde", foreground="#009", width=30).place(x=50,y=200)
#txt_Jogador2 = Entry(root, text="Jogador 2:", background="#dde", foreground="#009", width=30).place(x=50,y=250)





root.mainloop()



def main():
    return 0

if __name__ == '__main__':
    main()