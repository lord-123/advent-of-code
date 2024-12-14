from util import *

ll = readlinesints("14.in")

WIDTH = 101
HEIGHT = 103

robots = []
for x in ll:
    px,py, vx,vy = x
    robots += [[[px,py], [vx,vy]]]

print(robots)

def step(robot):
    robot[0][0] += robot[1][0]
    robot[0][0] %= WIDTH
    robot[0][1] += robot[1][1]
    robot[0][1] %= HEIGHT
    return robot

def sim(robot, seconds):
    for _ in range(seconds):
        robot = step(robot)
    return robot

new = [sim(r, 100) for r in robots]
#print(Counter([tuple(x[0]) for x in new]))

q1 = [x for x in new if x[0][0] < WIDTH // 2 and x[0][1] < HEIGHT // 2]
q2 = [x for x in new if x[0][0] > WIDTH // 2 and x[0][1] < HEIGHT // 2]
q3 = [x for x in new if x[0][0] < WIDTH // 2 and x[0][1] > HEIGHT // 2]
q4 = [x for x in new if x[0][0] > WIDTH // 2 and x[0][1] > HEIGHT // 2]

#print(q1,q2,q3,q4)
print(len(q1) * len(q2) * len(q3) * len(q4))

def draw(robots):
    s = []
    for y in range(HEIGHT):
        s += [["."] * WIDTH]
    #s = [["."] * WIDTH]
    for (px, py), _ in robots:
        #print(px,py)
        s[py][px] = "#"
    print("\n".join(lmap("".join, s)))

# FUCKING POINTERS ARE THE WORST PYTHON FEATURE
robots = []
for x in ll:
    px,py, vx,vy = x
    robots += [[[px,py], [vx,vy]]]

run = True
i = 1
while run:
    robots = [step(r) for r in robots]
    p = set(tuple(x[0]) for x in robots)
    for r in p:
        # look for a straight line
        if all([(r[0]+d, r[1]) in p for d in range(10)]):
            print(i)
            draw(robots)
            run=False
            break
    i+=1