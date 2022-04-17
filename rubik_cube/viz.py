# Importation de différentes bibliothèques
from tkinter import *
import cube
import encode_cube as en
from random import *
import threading
import time
import random
import shutil
import os
import re
import sys

    
global path_pddl, problem_file_path, plan_file_path, actions_list, plan_actions, en_var

path_pddl_model = '3x3/problems/model_problem.pddl'
path_pddl = '3x3/problems/sample_test.pddl'


def actions_from_plan():
    
    print('\n ----- Performing actions from the Plan File ----- \n')
    time.sleep(1)
    print("Number of steps to solution = ", len(plan_actions))
    for i in plan_actions:
        print('action: '+i)
        actions_dict[i]()
        time.sleep(1)
    
    print('\n ----- Cube Solved ----- \n')
    
def random_state():
    print("--- Shuffling the cube ---")
    for i in range(5):
        func = random.choice(actions_list)
        func()

def write_to_pddl():
    line_to_append = en.search_init(path_pddl,'(:init') + 2
    with open(path_pddl, 'r') as f:
        lines = f.readlines()

    for var in en_var:
        lines.insert(line_to_append, var)
        line_to_append += 1

    with open(path_pddl, 'w') as f:
        lines = "".join(lines)
        f.write(lines)
    f.close()


def fast_downward(path):
    print('----- Running Fast-Downward Planner ------')
    
    problem_path = path+'/problem.pddl'
    domain_path = path+'/domain.pddl'
    
    cwd = os.getcwd()
    print(cwd)
    
    shutil.copy( path_pddl, problem_path )
    shutil.copy( '3x3/cube_3x3.pddl', domain_path)
    
    os.chdir(path)
    print(os.getcwd())
    print(os.system('./fast-downward.py --plan-file plan_file.txt domain.pddl problem.pddl --search "astar(ff())"'))
    shutil.copy('plan_file.txt',cwd+'/3x3/plans/sample_test_downward.txt')
    os.chdir(cwd)

def extract_plans( path ):
    plan_actions = []
    with open(path, 'r') as plan_file:
        for line in plan_file:
            if 'cost' in line:
                break
            
            action = re.search('\((.*) \)',line)
            plan_actions.append(action.group(1).capitalize())  
    return plan_actions 


def choose_plan():
    # choice_of_planner = input('Chose the planner to solve the planner (0/1): ')
    choice_of_planner = 0
    if choice_of_planner == 0:
        planner_path = input("Enter Fast-Downward Path: ")
        fast_downward(planner_path)
        print('\n ------ Solution Found ------ \n')
        # global plan_actions 
        plan_actions = extract_plans('3x3/plans/sample_test_downward.txt')
        return plan_actions


close = Button(cube.window, text="Exit", bg='SlateGray1' , bd= 10 , activebackground ='red',command=cube.window.destroy)
close_window = cube.fond.create_window(40, 20, window=close)

# Titre
phrase = Label(cube.fond, text="Rubik's cube", fg='black' , bg ='#E4E4E4' , font= "Helvetica 36 bold")
phrase.pack()
cube.fond.create_window(700, 590, window=phrase)

actions_list = [cube.U,cube.Urev,cube.D,cube.Drev,cube.F,cube.Frev,cube.B,cube.Brev,cube.R,cube.Rrev,cube.L,cube.Lrev]
actions_dict = { 'U': cube.U,'Urev': cube.Urev,'D': cube.D,'Drev': cube.Drev,'F': cube.F,'Frev': cube.Frev,
                 'B': cube.B,'Brev': cube.Brev,'R': cube.R,'Rrev': cube.Rrev,'L': cube.L,'Lrev': cube.Lrev }

cube.AfficheGraphique3D()

if len(sys.argv) == 3:
    problem_file_path = sys.argv[1]
    plan_file_path = sys.argv[2]
    en.pddl_to_viz(problem_file_path)
    plan_actions = extract_plans(plan_file_path)
    th = threading.Thread(target=actions_from_plan)
    th.start()
elif len(sys.argv) == 2:
    problem_file_path = sys.argv[1]
    en.pddl_to_viz(problem_file_path)
    shutil.copy(problem_file_path,path_pddl)
    plan_actions = choose_plan()
    th = threading.Thread(target=actions_from_plan)
    th.start()
else:
    random_state() 
    shutil.copy( path_pddl_model, path_pddl )
    en_var = en.to_pddl()
    write_to_pddl()
    plan_actions = choose_plan()
    th = threading.Thread(target=actions_from_plan)
    th.start()

cube.window.mainloop() 
