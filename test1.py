#Projet: pjt libre
#Auteur: Cyrano Succar, Lilian Blet, Elise Romero--Goux

from pyxel import*
from class_perso import*
from class_plateforme import*
from class_sol import*
from time import*
#RAJOUTER SOL
class App:
    def __init__(self, nom_fichier, coord): #coord doit etre donné sous la forme [x,y]
        init(256, 256, title="Projet Libre")
        self.image=nom_fichier
        self.perso=Personnage(coord,1)
        self.ptf=Plateforme([150,170])
        self.s=Sol()
        run(self.update, self.draw)
    def update(self):
        if btn(KEY_D) or btn(KEY_RIGHT):
            if self.perso.pos[0]+5<224:
                self.perso.pos[0]+=5
        if btn(KEY_Q) or btn(KEY_LEFT):
            if self.perso.pos[0]-2>0:
                self.perso.pos[0]-=5
        if btnp(KEY_Z) or btnp(KEY_UP):
            self.perso.saut()
        if self.perso.pos[1]<self.s.sol:
            if not (self.perso.pos[1]+20==self.ptf.co[1] and self.perso.pos[0]-self.ptf.co[0]>=-26 and self.perso.pos[0]-self.ptf.co[0]<=63):
                self.perso.pos[1]+=self.perso.descente
        print('4',self.perso.pos[1])
        #faire un test qui verifie si on est sur une plateforme, sinon on descend(gere la descente du saut et la gravité)
        # créer une valeur, qui est- la somme des forces qui nous font descendre et monter et appliquer cette force
    def draw(self):
        load(self.image)
        cls(11)
        blt(self.perso.pos[0],self.perso.pos[1],0,0,0,32,32,13)
        blt(self.ptf.co[0],self.ptf.co[1],0,0,32,64,16,13)
        blt(0,241,0,0,48,15,15,13)
        blt(15,241,0,0,48,15,15,13)
        blt(30,241,0,0,48,15,15,13)
        blt(45,241,0,0,48,15,15,13)
        blt(60,241,0,0,48,15,15,13)
        blt(75,241,0,0,48,15,15,13)
        blt(90,241,0,0,48,15,15,13)
        blt(105,241,0,0,48,15,15,13)
        blt(120,241,0,0,48,15,15,13)
        blt(135,241,0,0,48,15,15,13)
        blt(150,241,0,0,48,15,15,13)
        blt(165,241,0,0,48,15,15,13)
        blt(180,241,0,0,48,15,15,13)
        blt(195,241,0,0,48,15,15,13)
        blt(210,241,0,0,48,15,15,13)
        blt(225,241,0,0,48,15,15,13)
        blt(240,241,0,0,48,15,15,13)
        blt(255,241,0,0,48,15,15,13)

App('res.pyxres',[0,210])