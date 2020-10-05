class Game(object):
    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self,count):
        self.__count=count
    @property
    def e(self):
        self.__e
    @e.setter
    def e(self,e):
        self.__e=e
    @property
    def secret(self):
        return self.__secret
    @secret.setter
    def secret(self,secret):
        self.__secret=secret
    def compare(self):
        while True:
            if self.__<self.__secret:
                self.__count=self.__count+1
                return"greater"
            if self.__e>self.__secret:
                self.__count=self.__count+1
                return"smaller"
            if self.__e==self.__secret:
                return "equal"
class Gameview(object):
    def __init__(self,root,guessgame):
        self.__root=root
        self.__guessgame=guessgame
        self.__root.title("Guess game")
        self.lb=Label(self.__root,text="Enter Your Guess From 1 to 10:")
        self.lb.grid(row=0,column=0)
        self.e=Entry(root)
        self.e.grid(row=1,column=2)
        self.cbt=Button(self.__root,text="Guess",command=self.guessit)
        self.cbt.grid(row=2,column=2)
        self.ybt=Button(self.__root,text="Clear",command=self.clear)
        self.ybt.grid(row=3,column=2)
    def guessit(self):
        estr=self.e.get()
        eint=int(estr)
        self.__guessgame.e=eint
        result=self.__guessgame.compare()
        while True:
            if result=="greater":
                self.lb.config(text="secret no is"+result+"than"+str(eint))
                break
            if result=="smaller":
                self.lb.config(text="secret no is"+result+"than"+str(eint))
                break
            if result=="equal":
                self.lb.config(text="Congratulations\n"+result+" to "+str(eint)+"\nguessing attempt was "+str(self.__guessgame.count))
                self.__guessgame.secret=random.randint(1,10)
                self.__guessgame.count=0
                break
    def clear(self):
        self.e.delete(0,END)
        self.lb.config(text="Enter Your Guess From 1 to 10:")
    def show(self):
        self.__root.mainloop()
class Gamecontroller(object):
    def __init__(self,model,view):
        self.__model=model
        self.__view=view
    def renderview(self):
        self.__view.show()
from tkinter import *
import random
gg=Game()
gg.secret=random.randint(1,10)
gg.count=0
v=Gameview(Tk(),gg)
c=Gamecontroller(gg,v)
c.renderview()
        



















        
        
