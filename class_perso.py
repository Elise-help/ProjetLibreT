#Projet: pjt libre
#Auteur: Cyrano Succar, Lilian Blet, Elise Romero--Goux
from time import*

class Personnage:
    def __init__(self, coordonnees,nv): #coordonnees a donner sous la forme [x,y]
        self.pos=coordonnees
        self.nv=nv
        self.h=0
        self.s=False
        self.descente=1
    def deplacement(self):
        if btn(KEY_D) or btn(KEY_RIGHT):
            self.pos[0]+=5
        if btn(KEY_Q) or btn(KEY_LEFT):
            self.pos[0]-=5
    def saut(self):
        self.s=True
        if self.h==0:
            self.h=self.pos[1]
            print('1',self.h)
            for i in range (20):
                print('5',self.h)
                self.h-=2
        while self.pos[1]>self.h:
            self.pos[1]-=1
            print('2',self.pos[1])
        self.h=0
        self.s=False
        print('3',self.pos[1])
       
#             self.pos[1]+=2