We have PDDL description for 1D, 2D and 3D Rubik's Cube,(RC) their plans and resources
to run with off-the-shelf planners 

Sub-directories
1. 1D-rubik
2. 2D-rubik: 2x2
3. 3D-rubik: 3x3 this is the usual RC that one refers to.

### Environment

1. python 2.7.18
2. Tkinter 8.6
3. Fast-Downward Planner


### Steps for Rubik's Cube Visualisation 

1. Please Clone this repository.
2. Install the [Fast-Downward](https://www.fast-downward.org/ObtainingAndRunningFastDownward) planner
3. Install the required libraries - Tkinter\
 - *For ubuntu*
    >sudo apt-get install python3-tk\
 - *For mac*
    >brew install python-tk
4. Run the Visualizer
 - *Case 1* - With no problem_file and plan_file
    - Runs problem_file - *'3x3/problems/cube_test3x3.pddl'* || plan_file - *'3x3/problems/cube_test3x3.txt'*
        >python3 viz.py
 - *Case 2* - With user defined problem_file
    - Takes in Planner location and Problem file as input arguments
    - The vizualizer is defined from the shuffled state of the cube from the provided problem file
        >python3 viz.py <\planner_path> <\problem_file path>\
        >python3 viz.py <\fast-downward-path> 3x3/problems/cube_test.pddl
 - *Case 3* - With user defined problem_file and already generated plan_file by Fast-Forward Planner
    - Takes in Problem file and Plan file as input arguments
    - The vizualizer is defined from the shuffled state of the cube from the provided problem file
        >python3 viz.py <\problem_file path> <\plan_file path>\
        >python3 viz.py 3x3/problems/cube_test.pddl 3x3/plans/cube_test.txt
 
