from util import *
# from z3 import *

ll = readlines("17.in")

# a,b,c = [int(ll[i].split(" ")[-1]) for i in (0,1,2)]

# #a = BitVec("a", 32)
program = ints(ll[-1])

# #def sim(a,b,c, program):
# o = []

# combo = {
#     0: lambda: 0,
#     1: lambda: 1,
#     2: lambda: 2,
#     3: lambda: 3,
#     4: lambda: a,
#     5: lambda: b,
#     6: lambda: c
# }

# def adv(op):
#     global a
#     a >>= combo[op]()

# def bxl(op):
#     global b
#     b ^= op

# def bst(op):
#     global b
#     b = combo[op]() & 0x07

# def jnz(op):
#     global pc
#     if a != 0:
#         pc = op-2

# def bxc(op):
#     global b
#     b ^= c

# def out(op):
#     global o
#     o += [combo[op]() & 0x07]

# def bdv(op):
#     global b
#     b = a >> combo[op]()

# def cdv(op):
#     global c
#     c = a >> combo[op]()

# instructions = {
#     0: adv,
#     1: bxl,
#     2: bst,
#     3: jnz,
#     4: bxc,
#     5: out,
#     6: bdv,
#     7: cdv
# }

# # pc = 0
# # while pc < len(program):
# #     instructions[program[pc]](program[pc+1])
# #     pc += 2

# # print(o)

# def run(regs, program):
#     a,b,c = regs
#     pc = 0
#     o = []

#     def combo(x):
#         return x if x <= 3 else [a,b,c][x-4]

#     while pc < len(program):
#         instruction, op = program[pc:pc+2]
#         pc += 2
#         #print(instruction, op, combo[op]())
#         #print(a,b,c)
#         match instruction:
#             case 0: a >>= combo(op)
#             case 1: b ^= op
#             case 2: b = combo(op) & 0x07
#             case 3: pc = (op if a != 0 else pc)
#             case 4: b ^= c
#             case 5:
#                 o += [combo(op) & 0x07]
#                 #print(combo(op))
#             case 6: b = a >> combo(op)
#             case 7: c = a >> combo(op)
        
#     return o

# # p1
# print(run((a,b,c), program))

# SPECIFIC TO MY INPUT
"""
B = A & 0x07
B ^= 2
C = A >> B
B ^= 3
B ^= C
OUT += [B & 0x07]
A >>= 3
Jump to start if A == 0

B = A & 0x07
B = (A & 0x07) ^ 2
C = A >> ((A & 0x07) ^ 2)
B = ((A & 0x07) ^ 2) ^ 3
B = (((A & 0x07) ^ 2) ^ 3) ^ (A >> ((A & 0x07) ^ 2))

"""

# p1
def s(a = 48744869):
    #a = 48744869
    if a == 0: return [None]
    o = []
    while a != 0:
        o += [(((a & 0x07) ^ 2) ^ 3) ^ (a >> ((a & 0x07) ^ 2)) & 0x07]
        a >>= 3
    return o
# p1
print(",".join(map(str, s())))

i = 0
for x in program[::-1]:
    i <<= 3
    r = s(i)
    while not all(a == b for a,b in zip(s(i)[::-1], program[::-1])):
        i += 1
# p2
print(i)