import requests, sys

if (len(sys.argv) <= 1) :
    domain_file = 'data/domain-hanoi.pddl'
    problem_file = 'data/problems/hanoi-3-2.pddl'
    output_file = 'data/plans/plan-hanoi-3-2.txt'
else:
    domain_file = sys.argv[1]
    problem_file = sys.argv[2]
    output_file = sys.argv[3]

print (f"Calling planner with domain - {domain_file}, problem - {problem_file}. Output will be in - {output_file}")

data = {'domain': open(domain_file, 'r').read(),
        'problem': open(problem_file, 'r').read()}

resp = requests.post('http://solver.planning.domains/solve',
                     verify=False, json=data).json()

with open(output_file, 'w') as f:
    f.write('\n'.join([act['name'] for act in resp['result']['plan']]))