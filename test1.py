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
        if self.perso.pos[1]<self.s.sol and (self.perso.pos[1]+20!=self.ptf.co[1] and self.perso.pos[0]+20!=self.ptf.co[0] and self.perso.pos[0]!=self.ptf.co[0]): #ajouter or plateforme
            self.perso.pos[1]+=self.perso.descente
        print('4',self.perso.pos[1])
        #faire un test qui verifie si on est sur une plateforme, sinon on descend(gere la descente du saut et la gravité)
        # créer une valeur, qui est- la somme des forces qui nous font descendre et monter et appliquer cette force
    def draw(self):
        load(self.image)
        cls(11)
        blt(self.perso.pos[0],self.perso.pos[1],0,0,0,32,32,13)
        blt(self.ptf.co[0],self.ptf.co[1],0,0,32,64,16,13)

App('res.pyxres',[0,210])