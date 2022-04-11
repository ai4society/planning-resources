We have PDDL description for 1D, 2D and 3D Rubik's Cube,(RC) their plans and resources
to run with off-the-shelf planners 

Sub-directories
1. 1D-rubik
2. 2D-rubik: 2x2
3. 3D-rubik: 3x3 this is the usual RC that one refers to.

### Steps for Rubik's Cube Visualisation 

1. Please Clone this repository.
2. Install the [Fast-Downward](https://www.fast-downward.org/ObtainingAndRunningFastDownward) planner
3. Install the required libraries - Tkinter
> sudo apt-get install python-tk
4. Run the Visualizer
> Run python viz.py

### Info regarding viz.py

- At every new instance of the code, the cube is shuffled
  - The PDDL of the suffled state of the cube is saved in *'3x3/problems/sample_test.pddl'*
- Runs Fast-Downward and Fast-Forward planner upon the choice of the user on the above mentioned problem file
- The plan files are stored in *'3x3/plans/'* folder.
