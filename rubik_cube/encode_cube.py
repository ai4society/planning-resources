from tkinter import *
import cube
from random import *

global cube1,cube2,cube3,cube4,cube5,cube6,cube7,cube8
global edge12,edge13,edge15,edge24,edge26,edge34,edge37,edge48,edge56,edge57,edge68,edge78
global var_to_append

dict_colors = { cube.red: 'R', cube.orange: 'O', cube.white: 'W', cube.green: 'G', cube.yellow: 'Y', cube.blue: 'B' }
color_object = {v: k for k, v in dict_colors.items()}

def search_init(file_path,string):
    with open(file_path, 'r') as f:
        line_number = 0
        for line in f:
            if string in line:
                return line_number
            line_number += 1

def to_pddl():

    cube1 = '(cube1 '+dict_colors[ cube.CC[0][0][0] ] + ' ' +dict_colors[ cube.CC[2][0][0] ]+ ' ' +dict_colors[ cube.CC[4][0][2] ]+')\n'
    cube2 = '(cube2 '+dict_colors[ cube.CC[1][2][2] ] + ' ' +dict_colors[ cube.CC[2][0][2] ]+ ' ' +dict_colors[ cube.CC[4][0][0] ]+')\n'
    cube3 = '(cube3 '+dict_colors[ cube.CC[0][2][0] ] + ' ' +dict_colors[ cube.CC[5][0][2] ]+ ' ' +dict_colors[ cube.CC[4][2][2] ]+')\n'
    cube4 = '(cube4 '+dict_colors[ cube.CC[1][2][0] ] + ' ' +dict_colors[ cube.CC[5][0][0] ]+ ' ' +dict_colors[ cube.CC[4][2][0] ]+')\n'
    cube5 = '(cube5 '+dict_colors[ cube.CC[0][0][2] ] + ' ' +dict_colors[ cube.CC[2][2][0] ]+ ' ' +dict_colors[ cube.CC[3][0][0] ]+')\n'
    cube6 = '(cube6 '+dict_colors[ cube.CC[1][0][2] ] + ' ' +dict_colors[ cube.CC[2][2][2] ]+ ' ' +dict_colors[ cube.CC[3][0][2] ]+')\n'
    cube7 = '(cube7 '+dict_colors[ cube.CC[0][2][2] ] + ' ' +dict_colors[ cube.CC[5][2][2] ]+ ' ' +dict_colors[ cube.CC[3][2][0] ]+')\n'
    cube8 = '(cube8 '+dict_colors[ cube.CC[1][0][0] ] + ' ' +dict_colors[ cube.CC[5][2][0] ]+ ' ' +dict_colors[ cube.CC[3][2][2] ]+')\n'

    edge12 = '(edge12 '+dict_colors[ cube.CC[2][0][1] ]+ ' ' +dict_colors[ cube.CC[4][0][1] ]+')\n'
    edge24 = '(edge24 '+dict_colors[ cube.CC[1][2][1] ]+ ' ' +dict_colors[ cube.CC[4][1][0] ]+')\n'
    edge34 = '(edge34 '+dict_colors[ cube.CC[5][0][1] ]+ ' ' +dict_colors[ cube.CC[4][2][1] ]+')\n'
    edge13 = '(edge13 '+dict_colors[ cube.CC[0][1][0] ]+ ' ' +dict_colors[ cube.CC[4][1][2] ]+')\n'

    edge15 = '(edge15 '+dict_colors[ cube.CC[0][0][1] ]+ ' ' +dict_colors[ cube.CC[2][1][0] ]+')\n'
    edge26 = '(edge26 '+dict_colors[ cube.CC[1][1][2] ]+ ' ' +dict_colors[ cube.CC[2][1][2] ]+')\n'
    edge48 = '(edge48 '+dict_colors[ cube.CC[1][1][0] ]+ ' ' +dict_colors[ cube.CC[5][1][0] ]+')\n'
    edge37 = '(edge37 '+dict_colors[ cube.CC[0][2][1] ]+ ' ' +dict_colors[ cube.CC[5][1][2] ]+')\n'

    edge56 = '(edge56 '+dict_colors[ cube.CC[2][2][1] ]+ ' ' +dict_colors[ cube.CC[3][0][1] ]+')\n'
    edge68 = '(edge68 '+dict_colors[ cube.CC[1][0][1] ]+ ' ' +dict_colors[ cube.CC[3][1][2] ]+')\n'
    edge78 = '(edge78 '+dict_colors[ cube.CC[5][2][1] ]+ ' ' +dict_colors[ cube.CC[3][2][1] ]+')\n'
    edge57 = '(edge57 '+dict_colors[ cube.CC[0][1][2] ]+ ' ' +dict_colors[ cube.CC[3][1][0] ]+')\n'

    var_to_append = [cube1,cube2,cube3,cube4,cube5,cube6,cube7,cube8,edge12,edge13,edge15,edge24,edge26,edge34,edge37,edge48,edge56,edge57,edge68,edge78 ]
    return var_to_append

def pddl_to_viz(problem_file_path):
    line_to_start = search_init(problem_file_path,'(:init')
    with open(problem_file_path, 'r') as f:
        lines = f.readlines()

    cube_lis = []
    edge_lis = []
    for line in lines[ line_to_start + 1: ]:
        
        if 'goal' in line:
            break
        
        if line.strip():
            string_strip = line.strip(' ').strip(')\n').strip('(')
            
            if 'cube' in string_strip:
                cube_lis.append(string_strip)
            elif 'edge' in string_strip:
                edge_lis.append(string_strip)
        
    for var in cube_lis:
        
        if 'cube1' in var:
            temp = var.strip('cube1 ').split(' ')
            cube.CC[0][0][0] = color_object[ temp[0] ]
            cube.CC[2][0][0] = color_object[ temp[1] ]
            cube.CC[4][0][2] = color_object[ temp[2] ]
            
        if 'cube2' in var:
            temp = var.strip('cube2 ').split(' ')
            cube.CC[1][2][2] = color_object[ temp[0] ]
            cube.CC[2][0][2] = color_object[ temp[1] ]
            cube.CC[4][0][0] = color_object[ temp[2] ]
            
        if 'cube3' in var:
            temp = var.strip('cube3 ').split(' ')
            cube.CC[0][2][0] = color_object[ temp[0] ]
            cube.CC[5][0][2] = color_object[ temp[1] ]
            cube.CC[4][2][2] = color_object[ temp[2] ]
            
        if 'cube4' in var:
            temp = var.strip('cube4 ').split(' ')
            cube.CC[1][2][0] = color_object[ temp[0] ]
            cube.CC[5][0][0] = color_object[ temp[1] ]
            cube.CC[4][2][0] = color_object[ temp[2] ]
            
        if 'cube5' in var:
            temp = var.strip('cube5 ').split(' ')
            cube.CC[0][0][2] = color_object[ temp[0] ]
            cube.CC[2][2][0] = color_object[ temp[1] ]
            cube.CC[3][0][0] = color_object[ temp[2] ]
            
        if 'cube6' in var:
            temp = var.strip('cube6 ').split(' ')
            cube.CC[1][0][2] = color_object[ temp[0] ]
            cube.CC[2][2][2] = color_object[ temp[1] ]
            cube.CC[3][0][2] = color_object[ temp[2] ]
            
        if 'cube7' in var:
            temp = var.strip('cube7 ').split(' ')
            cube.CC[0][2][2] = color_object[ temp[0] ]
            cube.CC[5][2][2] = color_object[ temp[1] ]
            cube.CC[3][2][0] = color_object[ temp[2] ]

        if 'cube8' in var:
            temp = var.strip('cube8 ').split(' ')
            cube.CC[1][0][0] = color_object[ temp[0] ]
            cube.CC[5][2][0] = color_object[ temp[1] ]
            cube.CC[3][2][2] = color_object[ temp[2] ]
            
    for var in edge_lis:
        
        if 'edge12' in var:
            temp = var.strip('edge12 ').split(' ')
            cube.CC[2][0][1] = color_object[ temp[0] ]
            cube.CC[4][0][1] = color_object[ temp[1] ]

        if 'edge24' in var:
            temp = var.strip('edge24 ').split(' ')
            cube.CC[1][2][1] = color_object[ temp[0] ]
            cube.CC[4][1][0] = color_object[ temp[1] ]
            
        if 'edge34' in var:
            temp = var.strip('edge34 ').split(' ')
            cube.CC[5][0][1] = color_object[ temp[0] ]
            cube.CC[4][2][1] = color_object[ temp[1] ]

        if 'edge13' in var:
            temp = var.strip('edge13 ').split(' ')
            cube.CC[0][1][0] = color_object[ temp[0] ]
            cube.CC[4][1][2] = color_object[ temp[1] ]
            
        if 'edge15' in var:
            temp = var.strip('edge15 ').split(' ')
            cube.CC[0][0][1] = color_object[ temp[0] ]
            cube.CC[2][1][0] = color_object[ temp[1] ]

        if 'edge26' in var:
            temp = var.strip('edge26 ').split(' ')
            cube.CC[1][1][2] = color_object[ temp[0] ]
            cube.CC[2][1][2] = color_object[ temp[1] ]
            
        if 'edge48' in var:
            temp = var.strip('edge48 ').split(' ')
            cube.CC[1][1][0] = color_object[ temp[0] ]
            cube.CC[5][1][0] = color_object[ temp[1] ]

        if 'edge37' in var:
            temp = var.strip('edge37 ').split(' ')
            cube.CC[0][2][1] = color_object[ temp[0] ]
            cube.CC[5][1][2] = color_object[ temp[1] ]
            
        if 'edge56' in var:
            temp = var.strip('edge56 ').split(' ')
            cube.CC[2][2][1] = color_object[ temp[0] ]
            cube.CC[3][0][1] = color_object[ temp[1] ]

        if 'edge68' in var:
            temp = var.strip('edge68 ').split(' ')
            cube.CC[1][0][1] = color_object[ temp[0] ]
            cube.CC[3][1][2] = color_object[ temp[1] ]
            
        if 'edge78' in var:
            temp = var.strip('edge78 ').split(' ')
            cube.CC[5][2][1] = color_object[ temp[0] ]
            cube.CC[3][2][1] = color_object[ temp[1] ]

        if 'edge57' in var:
            temp = var.strip('edge57 ').split(' ')
            cube.CC[0][1][2] = color_object[ temp[0] ]
            cube.CC[3][1][0] = color_object[ temp[1] ]

    cube.AfficheGraphique3D()
    
