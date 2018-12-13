from tkinter import *
from time import sleep
from random import choice

class Jogo:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("900x650+350+0")
        self.window.resizable(0,0)
        self.window.title("Pong")
        self.pontplayer = 0
        self.pontpc = 0
        self.movimentar = True

    
    def criatudo(self):
        self.canvas = Canvas(self.window, bg="#000", width=810, height=600)
        self.canvas.pack()
        self.create()
        self.window.bind("<Up>", self.moveUp)
        self.window.bind("<Down>", self.moveDown)
        self.window.bind("<m>", self.menu)
        self.window.bind("<M>", self.menu)
        self.x = 0
        self.y = 250
        self.vely = 50
        lista = [0.5,-1,1,-1,-1,-0.5]
        self.bally = choice(lista)
        listax = [6,-6]
        self.ballx = int(choice(listax))
        self.stop = False
        self.window.bind("<r>", self.restart)
        self.window.bind("<p>", self.unpause)
        self.window.bind("<R>", self.restart)
        self.window.bind("<P>", self.unpause)


    def parar(self, event=""):
        self.movimentar = False
        self.stop = True


    def restart(self, event):
        self.movimentar = True
        event = str(event)
        x = "keysym=r" in event
        y = "R" in event
        if x or y:
            self.pontpc = 0
            self.pontplayer = 0

        self.stop = False
        self.canvas.pack_forget()
        self.criatudo()
        self.init()

    
    def unpause(self, event):
        if self.stop == True:
            self.stop = False
            self.movimentar = True;
            self.init()
        else:
            self.stop = True
            self.movimentar = False


    def init(self):
        while True:
            self.moveBall()
            self.moveComputador()
            self.window.update()
            self.window.update_idletasks()
            sleep(0.01)
            if self.stop == True:
                break


    def create(self):
        self.player = self.canvas.create_rectangle(8,250,33,335, fill="#fff")
        self.computador = self.canvas.create_rectangle(775,250,800,335, fill="#fff")
        self.ball = self.canvas.create_oval(400, 270, 421,291, fill="#ecd814")
        self.texto = self.canvas.create_text(410,20, fill="#fff", text=f"player {self.pontplayer}  |  computador {self.pontpc}", font="Arial 18 bold")


    def moveUp(self, event):
        if self.movimentar:
            if self.y > 0:
                self.canvas.move(self.player, self.x, -self.vely)
                self.y = self.canvas.coords(self.player)[1]


    def moveDown(self, event):
        if self.movimentar:
            if self.y < 530:
                self.canvas.move(self.player, self.x, self.vely)
                self.y = self.canvas.coords(self.player)[1]


    def moveBall(self):
        coord = self.canvas.coords(self.ball)
        player_coord = self.canvas.coords(self.player)
        comp_coord = self.canvas.coords(self.computador)
        if  coord[0] > 5 and coord[0] < 800:
            if coord[1] <= 0:
                self.bally = 1
                self.canvas.move(self.ball, self.ballx, self.bally)

            elif coord[1] >= 550:
                self.bally = -1
                self.canvas.move(self.ball, self.ballx, self.bally)

            elif ((coord[0]>=player_coord[0]) and (coord[1] >= player_coord[1])) and ((coord[2] <=(player_coord[2]+5)) and (coord[3] <= player_coord[3])):
                self.ballx = -self.ballx
                self.canvas.move(self.ball, self.ballx, self.bally)

            elif ((coord[0] >= comp_coord[0]) and (coord[1] >= comp_coord[1])) and ((coord[2] <= comp_coord[2]+5) and (coord[3] <= comp_coord[3])):
                self.ballx = -self.ballx
                self.canvas.move(self.ball, self.ballx, self.bally)

            else:
                self.canvas.move(self.ball, self.ballx, self.bally)

        elif (coord[0] <= 5.0):
            self.pontuacao("computador")
            self.parar("inu")
            self.restart("dd")

        elif (coord[0] >= 800.0):
            self.pontuacao("player")
            self.parar("inu")
            self.restart("dd")


    def moveComputador(self):
        coord = self.canvas.coords(self.ball)
        comp_coord = self.canvas.coords(self.computador)
        if comp_coord[1] != (coord[1]-10):
            if comp_coord[1] > (coord[1]-10):
                self.compy = -0.96

            else:
                self.compy = 0.96

            self.canvas.move(self.computador, 0, self.compy)


    def pontuacao(self, ganhador):
        if ganhador == "player":
            self.pontplayer += 1

        else:
            self.pontpc += 1


    def comecar(self):
        self.menuexiste = True
        self.pontpc = 0
        self.pontplayer = 0
        self.frame = Frame(self.window, width=800, height=600, bg="#000")
        self.frame.pack()
        text = Label(self.frame, text="PONG!!!", bg="#000", fg="#fff", height=2, font="Arial 64 bold")
        text.place(x=237, y=0)
        btstart = Button(self.frame, borderwidth=0, text="Start", fg="#000", bg="#fff", font="Arial 20 bold", width=5, command=self.start)
        btstart.place(x=250, y=300)
        btquit = Button(self.frame, borderwidth=0, text="Quit", fg="#000", bg="#fff", font="Arial 20 bold", width=5, command=self.quit)
        btquit.place(x=455, y=300)
        creditos = Label(self.frame, text="@Buizzy - Eliezer de Almeida", bg="#000", fg="#fff", font="Arial 12 bold", height=2)
        creditos.place(x=550, y=550)


    def start(self):
        self.frame.pack_forget()
        self.menuexiste = False
        self.criatudo()
        self.init()


    def quit(self):
        self.stop = True
        self.window.destroy()


    def menu(self, event):
        if self.menuexiste == False:
            self.stop = True
            self.canvas.pack_forget()
            self.comecar()

