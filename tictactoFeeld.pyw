import tkinter as inter
from tkinter import messagebox as messagebox
import random

class guiap(inter.Tk):

    def __init__(self,parent):
        inter.Tk.__init__(self,parent)
        self.parent = parent
        self.feeld()
        self.spiel = game()
        self.protocol('WM_DELETE_WINDOW', self.clsPres)
        
    def feeld(self):
        self.geometry("900x600")
        self.xvariable = 15
        self.yvariable = 15
        self.buttons()
        self.names()
        self.configure(background='#222222')
        self.resizable(False,False)
        
        self.Name1.bind("<Any-KeyPress>", self.Setp1)
        self.Name2.bind("<Any-KeyPress>", self.Setp2)
        
    def Setp1(self, event):
        self.spiel.setPlayer1(self.Name1)
    def Setp2(self, event):
        self.spiel.setPlayer2(self.Name1)
    def names(self):
        self.LblConfig = inter.Label(self, bg="#555555")
        self.LblConfig.place(x = 600, y=0, width = 300, height = 600)
        self.name1lbl = inter.Label(self, text="Spieler1",bg="#555555",font=("Arial",16))
        self.name1lbl.place(x = 615, y=15)
        self.Name1 = inter.Entry(self, font=("Arial",14))
        self.Name1.place(x = 615, y= 45, width = 270, height = 30)
        self.name2lbl = inter.Label(self, text="Spieler2",bg="#555555",font=("Arial",16))
        self.name2lbl.place(x = 615, y=90)
        self.Name2 = inter.Entry(self, font=("Arial",14))
        self.Name2.place(x = 615, y= 120, width = 270, height = 30)
        self.restartbt = inter.Button(self,text="Restart",command=self.restart,font=("Arial",16))
        self.restartbt.place(x=615, y=555, height = 30)
        
    def buttons(self):
        self.bt1 = inter.Button(self,text="",command=self.exbt1,font=("Arial",44))
        self.bt1.place(x=self.xvariable, y=self.yvariable, width=170, height=170)
        self.upperX()
        self.bt2 = inter.Button(self,text="",command=self.exbt2,font=("Arial",44))
        self.bt2.place(x=self.xvariable, y=self.yvariable, width=170, height=170)
        self.upperX()
        self.bt3 = inter.Button(self,text="",command=self.exbt3,font=("Arial",44))
        self.bt3.place(x=self.xvariable, y=self.yvariable, width=170, height=170)
        self.xvariable = 15
        self.upperY()

        self.bt4 = inter.Button(self,text="",command=self.exbt4,font=("Arial",44))
        self.bt4.place(x=self.xvariable, y=self.yvariable, width=170, height=170)
        self.upperX()
        self.bt5 = inter.Button(self,text="",command=self.exbt5,font=("Arial",44))
        self.bt5.place(x=self.xvariable, y=self.yvariable, width=170, height=170)
        self.upperX()
        self.bt6 = inter.Button(self,text="",command=self.exbt6,font=("Arial",44))
        self.bt6.place(x=self.xvariable, y=self.yvariable, width=170, height=170)
        self.xvariable = 15
        self.upperY()

        self.bt7 = inter.Button(self,text="",command=self.exbt7,font=("Arial",44))
        self.bt7.place(x=self.xvariable, y=self.yvariable, width=170, height=170)
        self.upperX()
        self.bt8 = inter.Button(self,text="",command=self.exbt8,font=("Arial",44))
        self.bt8.place(x=self.xvariable, y=self.yvariable, width=170, height=170)
        self.upperX()
        self.bt9 = inter.Button(self,text="",command=self.exbt9,font=("Arial",44))
        self.bt9.place(x=self.xvariable, y=self.yvariable, width=170, height=170)

    def exbt1(self):
        if self.spiel.p1ID != "":
            self.bt1.config(text=self.spiel.pID)
            self.bt1.config(command=self.nothing)
            self.checkWin()
            self.spiel.zug()
        else:
            self.spiel.setID()
    def exbt2(self):
        if self.spiel.p1ID != "":
            self.bt2.config(text=self.spiel.pID)
            self.bt2.config(command=self.nothing)
            self.checkWin()
            self.spiel.zug()
        else:
            self.spiel.setID()
    def exbt3(self):
        if self.spiel.p1ID != "":
            self.bt3.config(text=self.spiel.pID)
            self.bt3.config(command=self.nothing)
            self.checkWin()
            self.spiel.zug()
        else:
            self.spiel.setID()
    def exbt4(self):
        if self.spiel.p1ID != "":
            self.bt4.config(text=self.spiel.pID)
            self.bt4.config(command=self.nothing)
            self.checkWin()
            self.spiel.zug()
        else:
            self.spiel.setID()
    def exbt5(self):
        if self.spiel.p1ID != "":
            self.bt5.config(text=self.spiel.pID)
            self.bt5.config(command=self.nothing)
            self.checkWin()
            self.spiel.zug()
        else:
            self.spiel.setID()
    def exbt6(self):
        if self.spiel.p1ID != "":
            self.bt6.config(text=self.spiel.pID)
            self.bt6.config(command=self.nothing)
            self.checkWin()
            self.spiel.zug()
        else:
            self.spiel.setID()
    def exbt7(self):
        if self.spiel.p1ID != "":
            self.bt7.config(text=self.spiel.pID)
            self.bt7.config(command=self.nothing)
            self.checkWin()
            self.spiel.zug()
        else:
            self.spiel.setID()
    def exbt8(self):
        if self.spiel.p1ID != "":
            self.bt8.config(text=self.spiel.pID)
            self.bt8.config(command=self.nothing)
            self.checkWin()
            self.spiel.zug()
        else:
            self.spiel.setID()
    def exbt9(self):
        if self.spiel.p1ID != "":
            self.bt9.config(text=self.spiel.pID)
            self.bt9.config(command=self.nothing)
            self.checkWin()
            self.spiel.zug()
        else:
            self.spiel.setID()
            
    def nothing(self):
        pass
    def checkWin(self):
        self.spiel.Check(self.bt1["text"], self.bt2["text"], self.bt3["text"],
                         self.bt4["text"], self.bt5["text"], self.bt6["text"],
                         self.bt7["text"], self.bt8["text"], self.bt9["text"])
    def upperX(self):
        self.xvariable +=200
    def upperY(self):
        self.yvariable +=200
    def restart(self):
        tmpp1 = self.spiel.player1
        tmpp2 = self.spiel.player2

        self.bt1.config(text="", command=self.exbt1)
        self.bt2.config(text="", command=self.exbt2)
        self.bt3.config(text="", command=self.exbt3)
        self.bt4.config(text="", command=self.exbt4)
        self.bt5.config(text="", command=self.exbt5)
        self.bt6.config(text="", command=self.exbt6)
        self.bt7.config(text="", command=self.exbt7)
        self.bt8.config(text="", command=self.exbt8)
        self.bt9.config(text="", command=self.exbt9)
        
        self.spiel = game()
        self.spiel.player1 = tmpp1
        self.spiel.player2 = tmpp2
        #inter.messagebox.showinfo("",self.winfo_geometry())
    def clsPres(self):
        exit()
#----------------------------------------------------------------------------------------------------------------
class game():
    def __init__(self):
        self.player1 = "Player 1"
        self.player2 = "Player 2"
        self.p1ID = ""
        self.p2ID = ""
        self.pID = "X"
        
    def setID(self):
        if  random.random() * 100 >= 50:
            self.p1ID = "X"
            self.p2ID = "O"
            messagebox.showinfo("start", self.player1 + " starts")
            #inter.Tk.message(text=self.player1 + " starts")
        else:
            self.p1ID = "O"
            self.p2ID = "X"
            messagebox.showinfo("start", self.player2 + " starts")
            #inter.Tk.message(text=self.player2 + " starts")
    def zug(self):
        if self.pID == "X":
            self.pID = "O"
        else:
            self.pID = "X"
            
    def setPlayer1(self, name):
        self.player1 = name.get()
    def setPlayer2(self, name):
        self.player2 = name.get()

    def Check(self, b1, b2, b3, b4, b5, b6, b7, b8, b9):
        if self.p1ID == self.pID:
            winner = self.player1
        else:
            winner = self.player2
        
        if (b1 != "" and b1 == b2 and b2 == b3) or (b4 !="" and b4 == b5 and b5==b6) or (b7 !="" and b7==b8 and b8==b9):
            messagebox.showinfo("Winn!", winner + " is the Winner!")
        elif (b1 != "" and b1 == b4 and b4 == b7) or (b2 !="" and b2 == b5 and b5==b8) or (b3 !="" and b3==b6 and b6==b9):
            messagebox.showinfo("Winn!", winner + " is the Winner!")
        elif (b1 != "" and b1 == b5 and b5 == b9) or (b7 !="" and b7 == b5 and b5==b3):
            messagebox.showinfo("Winn!", winner + " is the Winner!")
        elif b1 != "" and b2 != "" and b3 != "" and b4 != "" and b5 != "" and b6 != "" and b7 != "" and b8 != "" and b9 != "":
            messagebox.showinfo("END!", " Nobody winns")

#----------------------------------------------------------------------------------------------------------------
class launcher():
    def launch():
        spiel = guiap(None)
        spiel.title("Tic Tac Toe")
        spiel.iconbitmap('icon.ico')
        spiel.mainloop()
    def rlaunch(info):
        spiel = guiap(None)
        spiel.title("Tic Tac Toe")
        spiel.iconbitmap('icon.ico')
        spiel.mainloop()
        spiel.geometry(info)
#----------------------------------------------------------------------------------------------------------------
if __name__ =="__main__":
    launcher.launch()
    
