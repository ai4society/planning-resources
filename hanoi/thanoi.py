from turtle import *
import sys
dict_disk_peg = {"d1": " ","d2": " ","d3": " ","d4": " ","d5": " ","d6": " "}

if (len(sys.argv) <= 2) :
    plan_file = 'data/plans/plan-hanoi-3-2.txt'
else:
    plan_file = sys.argv[2]


class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) # square-->rectangle
        self.fillcolor(n/6., 0, 1-n/6.)
        self.st()
class Tower(list):
    def __init__(self, x):
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

# def hanoi(n, from_, to_):
# 	to_.push(from_.pop())

    # if n > 0:
    #     hanoi(n-1, from_, to_, with_)
    #     to_.push(from_.pop())
    #     hanoi(n-1, with_, from_, to_)

def find_tower(d):
    d1 = dict_disk_peg[d]
    if d1 in t1:
        return t1
    elif d1 in t2:
        return t2
    elif d1 in t3:
        return t3

def play():
    onkey(None,"space")
    clear()
    try:
        # hanoi(3, t1, t2, t3)
        pegs = {"peg3": t3,"peg2": t2,"peg1": t1}
        dict_ = {}
        for act in actions:
            print(act)

            # value = (8 - 2*dict_[act])
            # if value < 0:
            #     value = 0
            # hash_ = '#FF' + str(value) + '0' + str(value) +'0' 

            if act not in dict_:
                dict_[act] = 0
                color('black')
            else:
                dict_[act] += 1
                color('red')

            # color(hash_)
            write(act,align="center", font=("Courier", 16, "bold"))
            temp = act[1:-1].split(' ')
            from_ = temp[2]
            to_ = temp[3]

            if from_ in disk:
                temp_disk = from_
                from_ = find_tower(from_)
            else:
                from_ = pegs[from_]

            if to_ in disk:
                to_ = find_tower(to_)
            else:
                to_ = pegs[to_]

            to_.push(from_.pop())	
            clear()		

    except Terminator:
        pass  

def print_1():
    onkey(None,"1")
    clear()
    print("Entered 1")

def main():
    global t1, t2, t3
    ht();
    penup();
    goto(0, -225)   
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    pegs = {"peg3": t3,"peg2": t2,"peg1": t1}
    for i in range(int(sys.argv[1]),0,-1):
        temp_disk = "d" + str(i)
        t1.push(Disc(i))
        dict_disk_peg[temp_disk] = t1[-1]
    write("Press Space to Start",align="center", font=("Courier", 16, "bold"),)

    onkey(play, "space")
    
    onkey(print_1, "1")
    
    listen()
if __name__=="__main__":
    global pegs, disk, actions
    disk = set(['d1','d2','d3','d4','d5','d6'])
    actions = []
    with open(plan_file,'r') as f:
        for line in f:
            if line[-1] == "\n":
                actions.append(line[:-1])
            else:
                actions.append(line)

    msg = main()
    mainloop()