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

# path_pddl_model = '3x3/problems/model_problem.pddl'
# path_pddl = '3x3/problems/sample_test.pddl'


def actions_from_plan():
    
    actions = Label(cube.fond, text='Solution: ' +' '.join(plan_actions), fg='black' , bg ='#E4E4E4' , font= "Helvetica 22")
    cube.fond.create_window(500, 40, window=actions)
    
    print('\n ----- Performing actions from the Plan File ----- \n')
    time.sleep(1)
    print("Number of steps to solution = ", len(plan_actions))
    for i in plan_actions:
        actions_each = Label(cube.fond, text=i, fg='blue' , bg ='#E4E4E4' , font= "Helvetica 22")
        cube.fond.create_window(500, 550, window=actions_each)
        print('action: '+i)
        actions_dict[i]()
        time.sleep(1)
        actions_each.destroy()
    
    solved = Label(cube.fond, text='Cube Solved', fg='blue' , bg ='#E4E4E4' , font= "Helvetica 28 bold")
    cube.fond.create_window(500, 550, window=solved)
    solve.destroy()
    print('\n ----- Cube Solved ----- \n')
    
# def random_state():
#     print("--- Shuffling the cube ---")
#     for i in range(5):
#         func = random.choice(actions_list)
#         func()

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

def extract_plans( path ):
    plan_actions = []
    with open(path, 'r') as plan_file:
        for line in plan_file:
            if 'cost' in line:
                break
            
            action = re.search('\((.*) \)',line)
            plan_actions.append(action.group(1).capitalize())  
    return plan_actions 

def fast_downward(path,problem_path):
    cube.AfficheGraphique3D()
    print('----- Running Fast-Downward Planner ------')
    planner_status = Label(cube.fond, text='Running Fast-Downward Planner --- Please wait till the solution is found', fg='red' , bg ='#E4E4E4' , font= "Helvetica 18 bold")
    cube.fond.create_window(500, 500, window=planner_status)
    
    # problem_path = path+'/problem.pddl'
    # domain_path = path+'/domain.pddl'
    
    cwd = os.getcwd()
    print(cwd)
    domain_file = cwd+'/3x3/cube_3x3.pddl'
    problem_file = cwd+'/'+problem_path
    plan_file = cwd + '/3x3/plans/sample_test_downward.txt'
    exec_command = f'./fast-downward.py --plan-file {plan_file} {domain_file} {problem_file} --search "astar(ff())"'
    # shutil.copy( path_pddl, problem_path )
    # shutil.copy( '3x3/cube_3x3.pddl', domain_path)
    
    os.chdir(path)
    print(os.getcwd())
    print(os.system(exec_command))
    print('\n ------ Solution Found ------ \n')
    planner_status.destroy()
    planner_status = Label(cube.fond, text='Solution Found --> Click Solve to solve the cube', fg='blue' , bg ='#E4E4E4' , font= "Helvetica 20 bold")
    cube.fond.create_window(500, 500, window=planner_status)
    # shutil.copy('plan_file.txt',cwd+'/3x3/plans/sample_test_downward.txt')
    os.chdir(cwd)

def threading_actions():
    th = threading.Thread(target=actions_from_plan)
    th.start()

close = Button(cube.window, text="Exit", bg='SlateGray1' , bd= 10 , activebackground ='red',command=cube.window.destroy)
close_window = cube.fond.create_window(40, 20, window=close)

solve = Button(cube.window, text="Solve", bg='Green' , bd= 10 , activebackground ='blue',command=threading_actions)
solve_window = cube.fond.create_window(500, 600, window=solve)

# Titre
phrase = Label(cube.fond, text="Rubik's cube", fg='black' , bg ='#E4E4E4' , font= "Helvetica 36 bold")
phrase.pack()
cube.fond.create_window(500, 700, window=phrase)

actions_list = [cube.U,cube.Urev,cube.D,cube.Drev,cube.F,cube.Frev,cube.B,cube.Brev,cube.R,cube.Rrev,cube.L,cube.Lrev]
actions_dict = { 'U': cube.U,'Urev': cube.Urev,'D': cube.D,'Drev': cube.Drev,'F': cube.F,'Frev': cube.Frev,
                 'B': cube.B,'Brev': cube.Brev,'R': cube.R,'Rrev': cube.Rrev,'L': cube.L,'Lrev': cube.Lrev }

cube.AfficheGraphique3D()

if len(sys.argv) == 3:
    if '.pddl' in sys.argv[1]:
        problem_file_path = sys.argv[1]
        plan_file_path = sys.argv[2]
        en.pddl_to_viz(problem_file_path)
        plan_actions = extract_plans(plan_file_path)
    else:
        planner_path = sys.argv[1]
        problem_file_path = sys.argv[2]
        en.pddl_to_viz(problem_file_path)
        fast_downward(planner_path, problem_file_path)
        plan_actions = extract_plans('3x3/plans/sample_test_downward.txt')
# elif len(sys.argv) == 2:
#     problem_file_path = sys.argv[1]
#     en.pddl_to_viz(problem_file_path)
#     shutil.copy(problem_file_path,path_pddl)
#     plan_actions = extract_plans('3x3/plans/sample_test_downward.txt')
#     th = threading.Thread(target=actions_from_plan)
#     th.start()
else:
    en.pddl_to_viz('3x3/problems/cube_test3x3.pddl')
    plan_actions = extract_plans('3x3/plans/cube_test3x3.txt')

cube.window.mainloop() 
