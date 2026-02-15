#Projet: pjt libre
#Auteur: Cyrano Succar, Lilian Blet, Elise Romero--Goux
from time import*

class Personnage:
    def __init__(self, coordonnees,nv): #coordonnees a donner sous la forme [x,y]
        self.pos=coordonnees
        self.nv=nv
        self.h=0
        self.s=False
        self.x=0.5
#         for j in range(5):
#             self.x=self.x/2
        self.descente=1
    def deplacement(self):
        if btn(KEY_D) or btn(KEY_RIGHT):
            self.pos[0]+=5
        if btn(KEY_Q) or btn(KEY_LEFT):
            self.pos[0]-=5
    def saut(self): #frame
        self.s=True
        if self.h==0:
            self.h=self.pos[1]
            for i in range (10):
                print('1',self.h)
                self.h-=2
        while self.pos[1]>self.h:
            self.pos[1]-=self.x
            print('2',self.pos[1])
        self.h=0
        self.s=False
        print('3',self.pos[1])
       
#             self.pos[1]+=2
