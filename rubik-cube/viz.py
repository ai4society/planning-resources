# Importation de différentes bibliothèques
from Tkinter import *
from random import *
import threading
import time
import random
import shutil
import os
import re
################################################################## VARIABLES ##############################################################################

(couleur)=['red','blue','yellow','white','orange','green']

# cr est l'abréviation de cube résolu.

# Définition des couleurs
red='red'
orange='orange'
white='white'
green='green'
yellow='yellow'
blue='blue'

# Définition des listes
CC=[]  # Cube en cours (non résolu)
cm1=[] # Cube après le mouvement 1



# Partie graphique :

ag= 1

a = 800
b = 1100
i = int(a/12)
j = int(a/12)
x = int(a/22.5)
y = int(b/30)

fenetre = Tk()
fenetre.geometry(str(b)+"x"+str(a))
fond = Canvas(fenetre, width=b , heigh=a ,bg='#E4E4E4')
fond.pack(side=LEFT)

##################################################################### Functions ############################################################################
global path_pddl
path_pddl_model = '3x3/model_problem.pddl'
path_pddl = '3x3/sample_test.pddl'

shutil.copy(path_pddl_model,path_pddl)

dict_colors = { red: 'R', orange: 'O', white: 'W', green: 'G', yellow: 'Y', blue: 'B' }

def to_pddl():
    global cube1,cube2,cube3,cube4,cube5,cube6,cube7,cube8
    global edge12,edge13,edge15,edge24,edge26,edge34,edge37,edge48,edge56,edge57,edge68,edge78
    global var_to_append

    cube1 = '(cube1 '+dict_colors[ CC[0][0][0] ] + ' ' +dict_colors[ CC[2][0][0] ]+ ' ' +dict_colors[ CC[4][0][2] ]+')\n'
    cube2 = '(cube2 '+dict_colors[ CC[1][2][2] ] + ' ' +dict_colors[ CC[2][0][2] ]+ ' ' +dict_colors[ CC[4][0][0] ]+')\n'
    cube3 = '(cube3 '+dict_colors[ CC[0][2][0] ] + ' ' +dict_colors[ CC[5][0][2] ]+ ' ' +dict_colors[ CC[4][2][2] ]+')\n'
    cube4 = '(cube4 '+dict_colors[ CC[1][2][0] ] + ' ' +dict_colors[ CC[5][0][0] ]+ ' ' +dict_colors[ CC[4][2][0] ]+')\n'
    cube5 = '(cube5 '+dict_colors[ CC[0][0][2] ] + ' ' +dict_colors[ CC[2][2][0] ]+ ' ' +dict_colors[ CC[3][0][0] ]+')\n'
    cube6 = '(cube6 '+dict_colors[ CC[1][0][2] ] + ' ' +dict_colors[ CC[2][2][2] ]+ ' ' +dict_colors[ CC[3][0][2] ]+')\n'
    cube7 = '(cube7 '+dict_colors[ CC[0][2][2] ] + ' ' +dict_colors[ CC[5][2][2] ]+ ' ' +dict_colors[ CC[3][2][0] ]+')\n'
    cube8 = '(cube8 '+dict_colors[ CC[1][0][0] ] + ' ' +dict_colors[ CC[5][2][0] ]+ ' ' +dict_colors[ CC[3][2][2] ]+')\n'

    edge12 = '(edge12 '+dict_colors[ CC[2][0][1] ]+ ' ' +dict_colors[ CC[4][0][1] ]+')\n'
    edge24 = '(edge24 '+dict_colors[ CC[1][2][1] ]+ ' ' +dict_colors[ CC[4][1][0] ]+')\n'
    edge34 = '(edge34 '+dict_colors[ CC[5][0][1] ]+ ' ' +dict_colors[ CC[4][2][1] ]+')\n'
    edge13 = '(edge13 '+dict_colors[ CC[0][1][0] ]+ ' ' +dict_colors[ CC[4][1][2] ]+')\n'

    edge15 = '(edge15 '+dict_colors[ CC[0][0][1] ]+ ' ' +dict_colors[ CC[2][1][0] ]+')\n'
    edge26 = '(edge26 '+dict_colors[ CC[1][1][2] ]+ ' ' +dict_colors[ CC[2][1][2] ]+')\n'
    edge48 = '(edge48 '+dict_colors[ CC[1][1][0] ]+ ' ' +dict_colors[ CC[5][1][0] ]+')\n'
    edge37 = '(edge37 '+dict_colors[ CC[0][2][1] ]+ ' ' +dict_colors[ CC[5][1][2] ]+')\n'

    edge56 = '(edge56 '+dict_colors[ CC[2][2][1] ]+ ' ' +dict_colors[ CC[3][0][1] ]+')\n'
    edge68 = '(edge68 '+dict_colors[ CC[1][0][1] ]+ ' ' +dict_colors[ CC[3][1][2] ]+')\n'
    edge78 = '(edge78 '+dict_colors[ CC[5][2][1] ]+ ' ' +dict_colors[ CC[3][2][1] ]+')\n'
    edge57 = '(edge57 '+dict_colors[ CC[0][1][2] ]+ ' ' +dict_colors[ CC[3][1][0] ]+')\n'

    var_to_append = [cube1,cube2,cube3,cube4,cube5,cube6,cube7,cube8,edge12,edge13,edge15,edge24,edge26,edge34,edge37,edge48,edge56,edge57,edge68,edge78 ]
    

def CubeResolue() :
    global cr,red,orange,white,green,yellow,blue,CC
    cr=[[[red,red,red],[red,red,red],[red,red,red]],
        [[orange,orange,orange],[orange,orange,orange],[orange,orange,orange]],
        [[white,white,white],[white,white,white],[white,white,white]],
        [[green,green,green],[green,green,green],[green,green,green]],
        [[blue,blue,blue],[blue,blue,blue],[blue,blue,blue]],
        [[yellow,yellow,yellow],[yellow,yellow,yellow],[yellow,yellow,yellow]]]
    CC=cr

CubeResolue ()

# Fonction permettant l'affichage du Rubik's Cube en 3D

def AfficheGraphique3D ():
    
    c = 2*x
    d = 2*y
    
# Creation face1:

    F1C1=fond.create_polygon(c+4.32*x ,  d+2*y ,     c+2.66*x ,  d+2.66*y , c+1*x ,    d+2*y ,    c+2.66*x ,    d+1.34*y  ,outline='black' ,  fill=CC [0] [0] [0])
    F1C2=fond.create_polygon(c+5.98*x ,  d+2.66*y ,  c+4.32*x ,  d+3.33*y , c+2.66*x , d+2.66*y , c+4.32*x ,    d+2*y     ,outline='black' ,  fill=CC [0] [0] [1])
    F1C3=fond.create_polygon(c+7.66*x ,  d+3.34*y ,  c+6*x ,     d+4*y ,    c+4.32*x , d+3.33*y , c+5.98*x ,    d+2.66*y  ,outline='black' ,  fill=CC [0] [0] [2])
    F1C4=fond.create_polygon(c+5.98*x ,  d+1.34*y ,  c+4.32*x ,  d+2*y ,    c+2.66*x , d+1.34*y , c+4.32*x ,    d+0.66*y  ,outline='black' ,  fill=CC [0] [1] [0])
    F1C5=fond.create_polygon(c+7.66*x ,  d+2*y ,     c+5.98*x ,  d+2.66*y , c+4.32*x , d+2*y ,    c+5.98*x ,    d+1.34*y  ,outline='black' ,  fill=CC [0] [1] [1])
    F1C6=fond.create_polygon(c+9.32*x ,  d+2.67*y ,  c+7.66*x ,  d+3.34*y , c+5.98*x , d+2.66*y , c+7.64*x ,    d+2*y     ,outline='black' ,  fill=CC [0] [1] [2])
    F1C7=fond.create_polygon(c+7.66*x ,  d+0.66*y ,  c+5.98*x ,  d+1.34*y , c+4.32*x , d+0.67*y , c+6*x ,       d+0*y     ,outline='black' ,  fill=CC [0] [2] [0])
    F1C8=fond.create_polygon(c+9.32*x ,  d+1.33*y ,  c+7.64*x ,  d+2*y ,    c+5.98*x , d+1.34*y , c+7.66*x ,    d+0.66*y  ,outline='black' ,  fill=CC [0] [2] [1])
    F1C9=fond.create_polygon(c+11*x ,    d+2*y ,     c+9.32*x ,  d+2.67*y , c+7.64*x , d+2*y ,    c+9.32*x ,    d+1.33*y  ,outline='black' ,  fill=CC [0] [2] [2])

# Creation face 2 :

    F2C1=fond.create_polygon(c+22*x ,    d+2*y ,     c+20.32*x , d+2.67*y , c+18.64*x , d+2*y ,    c+20.32*x ,  d+1.33*y  ,outline='black' ,  fill=CC [1] [0] [0])
    F2C2=fond.create_polygon(c+20.32*x , d+2.67*y ,  c+18.66*x , d+3.34*y , c+16.98*x , d+2.66*y , c+18.64*x ,  d+2*y     ,outline='black' ,  fill=CC [1] [1] [0])
    F2C3=fond.create_polygon(c+18.66*x , d+3.34*y ,  c+17*x ,    d+4*y ,    c+15.32*x , d+3.33*y , c+16.98*x ,  d+2.66*y  ,outline='black' ,  fill=CC [1] [2] [0])
    F2C4=fond.create_polygon(c+20.32*x , d+1.33*y ,  c+18.64*x , d+2*y ,    c+16.98*x , d+1.34*y , c+18.66*x ,  d+0.66*y  ,outline='black' ,  fill=CC [1] [0] [1])
    F2C5=fond.create_polygon(c+18.66*x , d+2*y ,     c+16.98*x , d+2.66*y , c+15.32*x , d+2*y ,    c+16.98*x ,  d+1.34*y  ,outline='black' ,  fill=CC [1] [1] [1])
    F2C6=fond.create_polygon(c+16.98*x , d+2.66*y ,  c+15.32*x , d+3.33*y , c+13.66*x , d+2.66*y , c+15.32*x ,  d+2*y     ,outline='black' ,  fill=CC [1] [2] [1])
    F2C7=fond.create_polygon(c+18.66*x , d+0.66*y ,  c+16.98*x , d+1.34*y , c+15.32*x , d+0.67*y , c+17*x ,     d+0*y     ,outline='black' ,  fill=CC [1] [0] [2])
    F2C8=fond.create_polygon(c+16.98*x , d+1.34*y ,  c+15.32*x , d+2*y ,    c+13.66*x , d+1.34*y , c+15.32*x ,  d+0.67*y  ,outline='black' ,  fill=CC [1] [1] [2])
    F2C9=fond.create_polygon(c+15.32*x , d+2*y ,     c+13.66*x , d+2.66*y , c+12*x ,    d+2*y ,    c+13.66*x ,  d+1.34*y  ,outline='black' ,  fill=CC [1] [2] [2])    


# Creation face 3 :

    F3C1=fond.create_polygon(c+2.66*x ,  d+5.03*y ,  c+1*x ,     d+4.36*y ,  c+1*x ,    d+2*y ,    c+2.66*x ,   d+2.66*y  ,outline='black' ,  fill=CC [2] [0] [0])
    F3C2=fond.create_polygon(c+2.66*x ,  d+7.36*y ,  c+1*x ,     d+6.66*y ,  c+1*x ,    d+4.36*y , c+2.66*x ,   d+5.03*y  ,outline='black' ,  fill=CC [2] [0] [1])
    F3C3=fond.create_polygon(c+2.66*x ,  d+9.66*y ,  c+1*x ,     d+9*y ,     c+1*x ,    d+6.66*y , c+2.66*x ,   d+7.32*y  ,outline='black' ,  fill=CC [2] [0] [2])
    F3C4=fond.create_polygon(c+4.32*x ,  d+5.69*y ,  c+2.66*x ,  d+5.03*y ,  c+2.66*x , d+2.66*y , c+4.32*x ,   d+3.33*y  ,outline='black' ,  fill=CC [2] [1] [0])
    F3C5=fond.create_polygon(c+4.32*x ,  d+8.02*y ,  c+2.66*x ,  d+7.36*y ,  c+2.66*x , d+5.03*y , c+4.32*x ,   d+5.69*y  ,outline='black' ,  fill=CC [2] [1] [1])
    F3C6=fond.create_polygon(c+4.32*x ,  d+10.33*y , c+2.66*x ,  d+9.66*y ,  c+2.66*x , d+7.36*y , c+4.32*x ,   d+8.02*y  ,outline='black' ,  fill=CC [2] [1] [2])
    F3C7=fond.create_polygon(c+6*x ,     d+6.33*y ,  c+4.32*x ,  d+5.69*y ,  c+4.32*x , d+3.33*y , c+6*x ,      d+4*y     ,outline='black' ,  fill=CC [2] [2] [0])
    F3C8=fond.create_polygon(c+6*x ,     d+8.66*y ,  c+4.32*x ,  d+8.02*y ,  c+4.32*x , d+5.69*y , c+6*x ,      d+6.33*y  ,outline='black' ,  fill=CC [2] [2] [1])
    F3C9=fond.create_polygon(c+6*x ,     d+11*y ,    c+4.32*x ,  d+10.33*y , c+4.32*x , d+8.02*y , c+6*x ,      d+8.66*y  ,outline='black' ,  fill=CC [2] [2] [2])      

# Creation face 4 :

    F4C1=fond.create_polygon(c+7.66*x ,  d+5.69*y ,  c+6*x ,     d+6.33*y ,   c+6*x ,    d+4*y ,    c+7.66*x ,  d+3.33*y  ,outline='black' ,  fill=CC [3] [0] [0])
    F4C2=fond.create_polygon(c+7.66*x ,  d+8.02*y ,  c+6*x ,     d+8.66*y ,   c+6*x,     d+6.33*y , c+7.66*x,   d+5.69*y  ,outline='black' ,  fill=CC [3] [0] [1])
    F4C3=fond.create_polygon(c+7.66*x ,  d+10.33*y , c+6*x ,     d+11*y ,     c+6*x ,    d+8.66*y , c+7.66*x ,  d+8.02*y  ,outline='black' ,  fill=CC [3] [0] [2])
    F4C4=fond.create_polygon(c+9.32*x ,  d+5.04*y ,  c+7.66*x ,  d+5.7*y ,    c+7.66*x , d+3.34*y , c+9.32*x ,  d+2.67*y  ,outline='black' ,  fill=CC [3] [1] [0])
    F4C5=fond.create_polygon(c+9.32*x ,  d+7.34*y ,  c+7.66*x ,  d+8*y ,      c+7.66*x , d+5.7*y ,  c+9.32*x ,  d+5.04*y  ,outline='black' ,  fill=CC [3] [1] [1])
    F4C6=fond.create_polygon(c+9.32*x ,  d+9.67*y ,  c+7.66*x ,  d+10.33*y ,  c+7.66*x , d+8*y ,    c+9.32*x ,  d+7.33*y  ,outline='black' ,  fill=CC [3] [1] [2])
    F4C7=fond.create_polygon(c+11*x ,    d+4.36*y ,  c+9.32*x ,  d+5.04*y ,   c+9.32*x , d+2.67*y , c+11*x ,    d+2*y     ,outline='black' ,  fill=CC [3] [2] [0])
    F4C8=fond.create_polygon(c+11*x ,    d+6.67*y ,  c+9.32*x ,  d+7.34*y ,   c+9.32*x , d+5.04*y , c+11*x ,    d+4.36*y  ,outline='black' ,  fill=CC [3] [2] [1])
    F4C9=fond.create_polygon(c+11*x ,    d+9*y ,     c+9.32*x ,  d+9.67*y ,   c+9.32*x , d+7.33*y , c+11*x ,    d+6.66*y  ,outline='black' ,  fill=CC [3] [2] [2])
  
# Creation face 5   :

    F5C1=fond.create_polygon(c+18.66*x , d+5.66*y ,  c+17*x ,    d+6.33*y ,  c+17*x ,    d+4*y ,    c+18.66*x , d+3.33*y  ,outline='black' ,  fill=CC [5] [0] [0])
    F5C2=fond.create_polygon(c+18.66*x , d+8*y ,     c+17*x ,    d+8.66*y ,  c+17*x ,    d+6.33*y , c+18.66*x , d+5.66*y  ,outline='black' ,  fill=CC [5] [0] [1])
    F5C3=fond.create_polygon(c+18.66*x , d+10.33*y , c+17*x ,    d+11*y ,    c+17*x ,    d+8.66*y , c+18.66*x , d+8*y     ,outline='black' ,  fill=CC [5] [0] [2])
    F5C4=fond.create_polygon(c+20.32*x , d+5*y ,     c+18.66*x , d+5.66*y ,  c+18.66*x , d+3.33*y , c+20.32*x , d+2.66*y  ,outline='black' ,  fill=CC [5] [1] [0])
    F5C5=fond.create_polygon(c+20.32*x , d+7.33*y ,  c+18.66*x , d+8*y ,     c+18.66*x , d+5.66*y , c+20.32*x , d+5*y     ,outline='black' ,  fill=CC [5] [1] [1])
    F5C6=fond.create_polygon(c+20.32*x , d+9.66*y ,  c+18.66*x , d+10.33*y , c+18.66*x , d+8*y ,    c+20.32*x , d+7.33*y  ,outline='black' ,  fill=CC [5] [1] [2])
    F5C7=fond.create_polygon(c+22*x ,    d+4.36*y ,  c+20.32*x , d+5*y ,     c+20.32*x , d+2.66*y , c+22*x ,    d+2*y     ,outline='black' ,  fill=CC [5] [2] [0])
    F5C8=fond.create_polygon(c+22*x ,    d+6.66*y ,  c+20.32*x , d+7.33*y ,  c+20.32*x , d+5*y ,    c+22*x ,    d+4.36*y  ,outline='black' ,  fill=CC [5] [2] [1])
    F5C9=fond.create_polygon(c+22*x ,    d+9*y ,     c+20.32*x , d+9.66*y ,  c+20.32*x , d+7.33*y , c+22*x ,    d+6.66*y  ,outline='black' ,  fill=CC [5] [2] [2])
# Creation face 6 :

    F6C1=fond.create_polygon(c+13.66*x , d+5*y ,     c+12*x ,    d+4.36*y ,  c+12*x ,    d+2*y ,    c+13.66*x , d+2.66*y  ,outline='black' ,  fill=CC [4] [0] [0])
    F6C2=fond.create_polygon(c+13.66*x , d+7.32*y ,  c+12*x ,    d+6.66*y ,  c+12*x ,    d+4.36*y , c+13.66*x , d+5*y     ,outline='black' ,  fill=CC [4] [0] [1]) 
    F6C3=fond.create_polygon(c+13.66*x , d+9.66*y ,  c+12*x ,    d+9*y ,     c+12*x ,    d+6.66*y , c+13.66*x , d+7.32*y  ,outline='black' ,  fill=CC [4] [0] [2])
    F6C4=fond.create_polygon(c+15.32*x , d+5.66*y ,  c+13.66*x , d+5*y ,     c+13.66*x , d+2.66*y , c+15.32*x , d+3.33*y  ,outline='black' ,  fill=CC [4] [1] [0])
    F6C5=fond.create_polygon(c+15.32*x , d+8*y ,     c+13.66*x , d+7.32*y ,  c+13.66*x , d+5*y ,    c+15.32*x , d+5.66*y  ,outline='black' ,  fill=CC [4] [1] [1])  
    F6C6=fond.create_polygon(c+15.32*x , d+10.33*y , c+13.66*x , d+9.66*y ,  c+13.66*x , d+7.32*y , c+15.32*x , d+8*y     ,outline='black' ,  fill=CC [4] [1] [2])
    F6C7=fond.create_polygon(c+17*x ,    d+6.33*y ,  c+15.32*x , d+5.66*y ,  c+15.32*x , d+3.33*y , c+17*x ,    d+4*y     ,outline='black' ,  fill=CC [4] [2] [0])
    F6C8=fond.create_polygon(c+17*x ,    d+8.66*y ,  c+15.32*x , d+8*y ,     c+15.32*x , d+5.66*y , c+17*x ,    d+6.33*y  ,outline='black' ,  fill=CC [4] [2] [1])
    F6C9=fond.create_polygon(c+17*x ,    d+11*y ,    c+15.32*x , d+10.33*y , c+15.32*x , d+8*y ,    c+17*x ,    d+8.66*y  ,outline='black' ,  fill=CC [4] [2] [2])


    



def Opt_Affichage () :
    AfficheGraphique3D ()

    
def F():
    global CC,cm1
    cm1= [[[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[3][0][0]], [CC[1][1][0], CC[1][1][1], CC[3][0][1]], [CC[1][2][0], CC[1][2][1], CC[3][0][2]]], #orange    
          [[CC[2][0][2], CC[2][1][2], CC[2][2][2]], [CC[2][0][1], CC[2][1][1], CC[2][2][1]], [CC[2][0][0], CC[2][1][0], CC[2][2][0]]], #white    
          [[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[1][0][2], CC[1][1][2], CC[1][2][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow   
    CC=cm1
    Opt_Affichage ()
        
def Frev():
    global CC,cm2
    cm2= [[[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[4][0][0]], [CC[1][1][0], CC[1][1][1], CC[4][0][1]], [CC[1][2][0], CC[1][2][1], CC[4][0][2]]], #orange    
          [[CC[2][2][0], CC[2][1][0], CC[2][0][0]], [CC[2][2][1], CC[2][1][1], CC[2][0][1]], [CC[2][2][2], CC[2][1][2], CC[2][0][2]]], #white    
          [[CC[1][0][2], CC[1][1][2], CC[1][2][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow  
    CC=cm2

    Opt_Affichage ()



def B():
    global CC ,cm5
    cm5= [[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #red     
          [[CC[4][2][0], CC[1][0][1], CC[1][0][2]], [CC[4][2][1], CC[1][1][1], CC[1][1][2]], [CC[4][2][2], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[1][0][0], CC[1][1][0], CC[1][2][0]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #blue    
          [[CC[5][0][2], CC[5][1][2], CC[5][2][2]], [CC[5][0][1], CC[5][1][1], CC[5][2][1]], [CC[5][0][0], CC[5][1][0], CC[5][2][0]]]] #yellow   
    CC=cm5

    Opt_Affichage ()
        
def Brev():
    global CC,cm6
    cm6= [[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #red     
          [[CC[3][2][0], CC[1][0][1], CC[1][0][2]], [CC[3][2][1], CC[1][1][1], CC[1][1][2]], [CC[3][2][2], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[1][0][0], CC[1][1][0], CC[1][2][0]]], #blue    
          [[CC[5][2][0], CC[5][1][0], CC[5][0][0]], [CC[5][2][1], CC[5][1][1], CC[5][0][1]], [CC[5][2][2], CC[5][1][2], CC[5][0][2]]]] #yellow  
    CC=cm6
    Opt_Affichage ()
    

def D():
    global CC ,cm7
    cm7= [[[CC[5][0][2], CC[0][0][1], CC[0][0][2]], [CC[5][0][1], CC[0][1][1], CC[0][1][2]], [CC[5][0][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[2][0][2], CC[2][0][1], CC[2][0][0]]], #orange    
          [[CC[0][2][0], CC[0][1][0], CC[0][0][0]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[4][0][2], CC[4][1][2], CC[4][2][2]], [CC[4][0][1], CC[4][1][1], CC[4][2][1]], [CC[4][0][0], CC[4][1][0], CC[4][2][0]]], #blue    
          [[CC[1][2][2], CC[1][2][1], CC[1][2][0]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow  
    CC=cm7

    Opt_Affichage ()

def Drev():
    global CC ,cm8
    cm8= [[[CC[2][0][2], CC[0][0][1], CC[0][0][2]], [CC[2][0][1], CC[0][1][1], CC[0][1][2]], [CC[2][0][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[5][0][2], CC[5][0][1], CC[5][0][0]]], #orange    
          [[CC[1][2][2], CC[1][2][1], CC[1][2][0]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[4][2][0], CC[4][1][0], CC[4][0][0]], [CC[4][2][1], CC[4][1][1], CC[4][0][1]], [CC[4][2][2], CC[4][1][2], CC[4][0][2]]], #blue    
          [[CC[0][2][0], CC[0][1][0], CC[0][0][0]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow   

    CC=cm8

    Opt_Affichage ()
    

def U():
    global CC ,cm12
    cm12=[[[CC[0][0][0], CC[0][0][1], CC[2][2][2]], [CC[0][1][0], CC[0][1][1], CC[2][2][1]], [CC[0][2][0], CC[0][2][1], CC[2][2][0]]], #red     
          [[CC[5][2][2], CC[5][2][1], CC[5][2][0]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[1][0][2], CC[1][0][1], CC[1][0][0]]], #white    
          [[CC[3][0][2], CC[3][1][2], CC[3][2][2]], [CC[3][0][1], CC[3][1][1], CC[3][2][1]], [CC[3][0][0], CC[3][1][0], CC[3][2][0]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[0][2][2], CC[0][1][2], CC[0][0][2]]]] #yellow  
    CC=cm12

    Opt_Affichage ()
     
def Urev():
    global CC ,cm11
    cm11=[[[CC[0][0][0], CC[0][0][1], CC[5][2][2]], [CC[0][1][0], CC[0][1][1], CC[5][2][1]], [CC[0][2][0], CC[0][2][1], CC[5][2][0]]], #red     
          [[CC[2][2][2], CC[2][2][1], CC[2][2][0]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[0][2][2], CC[0][1][2], CC[0][0][2]]], #white    
          [[CC[3][2][0], CC[3][1][0], CC[3][0][0]], [CC[3][2][1], CC[3][1][1], CC[3][0][1]], [CC[3][2][2], CC[3][1][2], CC[3][0][2]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[1][0][2], CC[1][0][1], CC[1][0][0]]]] #yellow   

    CC=cm11

    Opt_Affichage ()


def R():
    global CC,cm13
    cm13=[[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][2], CC[1][1][2], CC[1][2][2]], [CC[1][0][1], CC[1][1][1], CC[1][2][1]], [CC[1][0][0], CC[1][1][0], CC[1][2][0]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[4][2][0]], [CC[2][1][0], CC[2][1][1], CC[4][1][0]], [CC[2][2][0], CC[2][2][1], CC[4][0][0]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[2][0][2]], [CC[3][1][0], CC[3][1][1], CC[2][1][2]], [CC[3][2][0], CC[3][2][1], CC[2][2][2]]], #green    
          [[CC[5][0][0], CC[4][0][1], CC[4][0][2]], [CC[5][1][0], CC[4][1][1], CC[4][1][2]], [CC[5][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[3][2][2], CC[5][0][1], CC[5][0][2]], [CC[3][1][2], CC[5][1][1], CC[5][1][2]], [CC[3][0][2], CC[5][2][1], CC[5][2][2]]]] #yellow  
    CC=cm13

    Opt_Affichage ()     
        
def Rrev():
    global CC,cm14
    cm14=[[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][2][0], CC[1][1][0], CC[1][0][0]], [CC[1][2][1], CC[1][1][1], CC[1][0][1]], [CC[1][2][2], CC[1][1][2], CC[1][0][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[3][0][2]], [CC[2][1][0], CC[2][1][1], CC[3][1][2]], [CC[2][2][0], CC[2][2][1], CC[3][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[5][2][0]], [CC[3][1][0], CC[3][1][1], CC[5][1][0]], [CC[3][2][0], CC[3][2][1], CC[5][0][0]]], #green    
          [[CC[2][2][2], CC[4][0][1], CC[4][0][2]], [CC[2][1][2], CC[4][1][1], CC[4][1][2]], [CC[2][0][2], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[4][0][0], CC[5][0][1], CC[5][0][2]], [CC[4][1][0], CC[5][1][1], CC[5][1][2]], [CC[4][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow   
    CC=cm14

    Opt_Affichage ()


def L():
    global CC,cm18
    cm18=[[[CC[0][0][2], CC[0][1][2], CC[0][2][2]], [CC[0][0][1], CC[0][1][1], CC[0][2][1]], [CC[0][0][0], CC[0][1][0], CC[0][2][0]]], #red
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange
          [[CC[3][0][0], CC[2][0][1], CC[2][0][2]], [CC[3][1][0], CC[2][1][1], CC[2][1][2]], [CC[3][2][0], CC[2][2][1], CC[2][2][2]]], #white
          [[CC[5][2][2], CC[3][0][1], CC[3][0][2]], [CC[5][1][2], CC[3][1][1], CC[3][1][2]], [CC[5][0][2], CC[3][2][1], CC[3][2][2]]], #green
          [[CC[4][0][0], CC[4][0][1], CC[2][2][0]], [CC[4][1][0], CC[4][1][1], CC[2][1][0]], [CC[4][2][0], CC[4][2][1], CC[2][0][0]]], #blue
          [[CC[5][0][0], CC[5][0][1], CC[4][0][2]], [CC[5][1][0], CC[5][1][1], CC[4][1][2]], [CC[5][2][0], CC[5][2][1], CC[4][2][2]]]] #yellow
    CC=cm18

    Opt_Affichage ()
    
def Lrev():
    global CC,cm17
    cm17=[[[CC[0][2][0], CC[0][1][0], CC[0][0][0]], [CC[0][2][1], CC[0][1][1], CC[0][0][1]], [CC[0][2][2], CC[0][1][2], CC[0][0][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[4][2][2], CC[2][0][1], CC[2][0][2]], [CC[4][1][2], CC[2][1][1], CC[2][1][2]], [CC[4][0][2], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[2][0][0], CC[3][0][1], CC[3][0][2]], [CC[2][1][0], CC[3][1][1], CC[3][1][2]], [CC[2][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[5][0][2]], [CC[4][1][0], CC[4][1][1], CC[5][1][2]], [CC[4][2][0], CC[4][2][1], CC[5][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[3][2][0]], [CC[5][1][0], CC[5][1][1], CC[3][1][0]], [CC[5][2][0], CC[5][2][1], CC[3][0][0]]]] #yellow   
    CC=cm17

    Opt_Affichage ()

    # cm17=[[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
    #       [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange    
    #       [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
    #       [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
    #       [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
    #       [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow   

def actions_from_plan():
    
    print('\n ----- Performing actions from the Plan File ----- \n')
    time.sleep(3)
    for i in plan_actions:
        print('action: '+i)
        eval(i+'()')
        time.sleep(1)
    
def random_state():

    print("--- Shuffling the cube ---")
    for i in range(10):
        func = random.choice(actions_list)
        func()


def search_init(file_path,string):
    with open(file_path, 'r') as f:
        line_number = 0
        for line in f:
            if string in line:
                return line_number
            line_number += 1

def write_to_pddl():
    line_to_append = search_init(path_pddl,'(:init') + 2
    with open(path_pddl, 'r') as f:
        lines = f.readlines()

    for var in var_to_append:
        lines.insert(line_to_append, var)
        line_to_append += 1

    with open(path_pddl, 'w') as f:
        lines = "".join(lines)
        f.write(lines)
    f.close()


def fast_downward():
    print('----- Running Fast-Downward Planner ------')
    os.chdir('../downward')
    print(os.getcwd())
    print(os.system('./fast-downward.py --plan-file ../rubiks_cube/3x3/sample_test_downward.txt ../rubiks_cube/3x3/cube_3x3.pddl ../rubiks_cube/3x3/sample_test.pddl --search "astar(ff())"'))
    os.chdir('../rubiks_cube')

def fast_forward():
    print('----- Running Fast-Forward Planner ------')
    os.chdir('../FF')
    print(os.getcwd())
    print(os.system('./ff -o ../rubiks_cube/3x3/cube_3x3.pddl -f ../rubiks_cube/3x3/sample_test.pddl > ../rubiks_cube/3x3/sample_test_ff.txt'))
    os.chdir('../rubiks_cube')

fermer = Button(fenetre, text="Exit", bg='SlateGray1' , bd= 10 , activebackground ='red',command=fenetre.destroy)
fermer_fenetre = fond.create_window(40, 20, window=fermer)

# Titre
phrase = Label(fond, text="Rubik's cube", fg='black' , bg ='#E4E4E4' , font= "Helvetica 36 bold")
phrase.pack()
fond.create_window(700, 590, window=phrase)

global actions_list
actions_list = [U,Urev,D,Drev,F,Frev,B,Brev,R,Rrev,L,Lrev]

AfficheGraphique3D ()
random_state()

to_pddl()
write_to_pddl()

fast_downward()
# fast_forward()


print('\n --- Solution Plan File options ---\n')
print('0: Fast-Downward \n1: Fast-Forward\n')

choice_of_planner = input('Chose the plan file (0/1): ')

if choice_of_planner == 0:
    
    global plan_actions 
    plan_actions = []
    with open('3x3/sample_test_downward.txt', 'r') as plan_file:
        for line in plan_file:
            if 'cost' in line:
                break
            
            action = re.search('\((.*) \)',line)
            plan_actions.append(action.group(1).capitalize())
    
    th = threading.Thread(target=actions_from_plan)
    th.start()

    fenetre.mainloop()


