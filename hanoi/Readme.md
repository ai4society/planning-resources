Credits:
- Domain taken from:
  https://github.com/SoarGroup/Domains-Planning-Domain-Definition-Language/tree/master/pddl

Command line param:
 - <\domain file> <\problem file> <\output file>
 - Example: data/domain-hanoi.pddl data/problems/hanoi-3.pddl data/plans/plan-hanoi-3.txt

For example, invoke with:
python3 APIPlannerInvoker.py data/domain-hanoi.pddl data/problems/hanoi-3.pddl data/plans/plan-hanoi-3.txt

1. Install required Libraries - turtle
>pip install PythonTurtle

### For visualization
1. Please generate the required plan by running *APIPlannerInvoker.py*
2. Run the following command 
- > python thanoi.py <\number_of_disks> <\plan file>

Example: >python thanoi.py 6 data/plans/plan-hanoi-6.txt
