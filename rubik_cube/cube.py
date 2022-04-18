from tkinter import *

red='red'
orange='orange'
white='white'
green='green'
yellow='yellow'
blue='blue'

# Définition des listes
global CC
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

window = Tk()
window.geometry(str(b)+"x"+str(a))
fond = Canvas(window, width=b , heigh=a ,bg='#E4E4E4')
fond.pack(side=LEFT)

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
    

def L():
    global CC ,cm7
    cm7= [[[CC[5][0][2], CC[0][0][1], CC[0][0][2]], [CC[5][0][1], CC[0][1][1], CC[0][1][2]], [CC[5][0][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[2][0][2], CC[2][0][1], CC[2][0][0]]], #orange    
          [[CC[0][2][0], CC[0][1][0], CC[0][0][0]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[4][0][2], CC[4][1][2], CC[4][2][2]], [CC[4][0][1], CC[4][1][1], CC[4][2][1]], [CC[4][0][0], CC[4][1][0], CC[4][2][0]]], #blue    
          [[CC[1][2][2], CC[1][2][1], CC[1][2][0]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow  
    CC=cm7

    Opt_Affichage ()

def Lrev():
    global CC ,cm8
    cm8= [[[CC[2][0][2], CC[0][0][1], CC[0][0][2]], [CC[2][0][1], CC[0][1][1], CC[0][1][2]], [CC[2][0][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[5][0][2], CC[5][0][1], CC[5][0][0]]], #orange    
          [[CC[1][2][2], CC[1][2][1], CC[1][2][0]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[2][2][0], CC[2][2][1], CC[2][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[3][0][2]], [CC[3][1][0], CC[3][1][1], CC[3][1][2]], [CC[3][2][0], CC[3][2][1], CC[3][2][2]]], #green    
          [[CC[4][2][0], CC[4][1][0], CC[4][0][0]], [CC[4][2][1], CC[4][1][1], CC[4][0][1]], [CC[4][2][2], CC[4][1][2], CC[4][0][2]]], #blue    
          [[CC[0][2][0], CC[0][1][0], CC[0][0][0]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[5][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow   

    CC=cm8

    Opt_Affichage ()
    

def R():
    global CC ,cm12
    cm12=[[[CC[0][0][0], CC[0][0][1], CC[2][2][2]], [CC[0][1][0], CC[0][1][1], CC[2][2][1]], [CC[0][2][0], CC[0][2][1], CC[2][2][0]]], #red     
          [[CC[5][2][2], CC[5][2][1], CC[5][2][0]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[1][0][2], CC[1][0][1], CC[1][0][0]]], #white    
          [[CC[3][0][2], CC[3][1][2], CC[3][2][2]], [CC[3][0][1], CC[3][1][1], CC[3][2][1]], [CC[3][0][0], CC[3][1][0], CC[3][2][0]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[0][2][2], CC[0][1][2], CC[0][0][2]]]] #yellow  
    CC=cm12

    Opt_Affichage ()
     
def Rrev():
    global CC ,cm11
    cm11=[[[CC[0][0][0], CC[0][0][1], CC[5][2][2]], [CC[0][1][0], CC[0][1][1], CC[5][2][1]], [CC[0][2][0], CC[0][2][1], CC[5][2][0]]], #red     
          [[CC[2][2][2], CC[2][2][1], CC[2][2][0]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[2][0][2]], [CC[2][1][0], CC[2][1][1], CC[2][1][2]], [CC[0][2][2], CC[0][1][2], CC[0][0][2]]], #white    
          [[CC[3][2][0], CC[3][1][0], CC[3][0][0]], [CC[3][2][1], CC[3][1][1], CC[3][0][1]], [CC[3][2][2], CC[3][1][2], CC[3][0][2]]], #green    
          [[CC[4][0][0], CC[4][0][1], CC[4][0][2]], [CC[4][1][0], CC[4][1][1], CC[4][1][2]], [CC[4][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[5][0][0], CC[5][0][1], CC[5][0][2]], [CC[5][1][0], CC[5][1][1], CC[5][1][2]], [CC[1][0][2], CC[1][0][1], CC[1][0][0]]]] #yellow   

    CC=cm11

    Opt_Affichage ()


def D():
    global CC,cm13
    cm13=[[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][0][2], CC[1][1][2], CC[1][2][2]], [CC[1][0][1], CC[1][1][1], CC[1][2][1]], [CC[1][0][0], CC[1][1][0], CC[1][2][0]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[4][2][0]], [CC[2][1][0], CC[2][1][1], CC[4][1][0]], [CC[2][2][0], CC[2][2][1], CC[4][0][0]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[2][0][2]], [CC[3][1][0], CC[3][1][1], CC[2][1][2]], [CC[3][2][0], CC[3][2][1], CC[2][2][2]]], #green    
          [[CC[5][0][0], CC[4][0][1], CC[4][0][2]], [CC[5][1][0], CC[4][1][1], CC[4][1][2]], [CC[5][2][0], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[3][2][2], CC[5][0][1], CC[5][0][2]], [CC[3][1][2], CC[5][1][1], CC[5][1][2]], [CC[3][0][2], CC[5][2][1], CC[5][2][2]]]] #yellow  
    CC=cm13

    Opt_Affichage ()     
        
def Drev():
    global CC,cm14
    cm14=[[[CC[0][0][0], CC[0][0][1], CC[0][0][2]], [CC[0][1][0], CC[0][1][1], CC[0][1][2]], [CC[0][2][0], CC[0][2][1], CC[0][2][2]]], #red     
          [[CC[1][2][0], CC[1][1][0], CC[1][0][0]], [CC[1][2][1], CC[1][1][1], CC[1][0][1]], [CC[1][2][2], CC[1][1][2], CC[1][0][2]]], #orange    
          [[CC[2][0][0], CC[2][0][1], CC[3][0][2]], [CC[2][1][0], CC[2][1][1], CC[3][1][2]], [CC[2][2][0], CC[2][2][1], CC[3][2][2]]], #white    
          [[CC[3][0][0], CC[3][0][1], CC[5][2][0]], [CC[3][1][0], CC[3][1][1], CC[5][1][0]], [CC[3][2][0], CC[3][2][1], CC[5][0][0]]], #green    
          [[CC[2][2][2], CC[4][0][1], CC[4][0][2]], [CC[2][1][2], CC[4][1][1], CC[4][1][2]], [CC[2][0][2], CC[4][2][1], CC[4][2][2]]], #blue    
          [[CC[4][0][0], CC[5][0][1], CC[5][0][2]], [CC[4][1][0], CC[5][1][1], CC[5][1][2]], [CC[4][2][0], CC[5][2][1], CC[5][2][2]]]] #yellow   
    CC=cm14

    Opt_Affichage ()


def U():
    global CC,cm18
    cm18=[[[CC[0][0][2], CC[0][1][2], CC[0][2][2]], [CC[0][0][1], CC[0][1][1], CC[0][2][1]], [CC[0][0][0], CC[0][1][0], CC[0][2][0]]], #red
          [[CC[1][0][0], CC[1][0][1], CC[1][0][2]], [CC[1][1][0], CC[1][1][1], CC[1][1][2]], [CC[1][2][0], CC[1][2][1], CC[1][2][2]]], #orange
          [[CC[3][0][0], CC[2][0][1], CC[2][0][2]], [CC[3][1][0], CC[2][1][1], CC[2][1][2]], [CC[3][2][0], CC[2][2][1], CC[2][2][2]]], #white
          [[CC[5][2][2], CC[3][0][1], CC[3][0][2]], [CC[5][1][2], CC[3][1][1], CC[3][1][2]], [CC[5][0][2], CC[3][2][1], CC[3][2][2]]], #green
          [[CC[4][0][0], CC[4][0][1], CC[2][2][0]], [CC[4][1][0], CC[4][1][1], CC[2][1][0]], [CC[4][2][0], CC[4][2][1], CC[2][0][0]]], #blue
          [[CC[5][0][0], CC[5][0][1], CC[4][0][2]], [CC[5][1][0], CC[5][1][1], CC[4][1][2]], [CC[5][2][0], CC[5][2][1], CC[4][2][2]]]] #yellow
    CC=cm18

    Opt_Affichage ()
    
def Urev():
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
