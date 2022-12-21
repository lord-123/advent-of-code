import operator
from z3 import *

with open("input", "r") as f:
	ll = f.read().split("\n")

ins = {}
for l in ll:
	p = l.split(" ")
	ins[p[0][:4]] = p[1:]

ops = {
	"+": operator.add,
	"-": operator.sub,
	"*": operator.mul,
	"/": operator.floordiv
}

def get_tree(start):
	if len(ins[start]) == 1:
		return { "literal": int(ins[start][0]) }

	return { "operator": ops[ins[start][1]],
			 "left": get_tree(ins[start][0]),
			 "right": get_tree(ins[start][2]) }

def eval_tree(tree):
	if "literal" in tree: return tree["literal"]

	return tree["operator"](eval_tree(tree["left"]), eval_tree(tree["right"]))

#p1
print("p1", eval_tree(get_tree("root")))

#p2
humn = Int("humn")
ins["root"][1] = "=="
ins["humn"][0] = "humn"
def get_tree_z3(start):
	if len(ins[start]) == 1:
		return {"literal": ins[start][0] }
	return { "operator": ins[start][1],
			 "left": get_tree_z3(ins[start][0]),
			 "right": get_tree_z3(ins[start][2]) }
def create_z3(tree):
	#print(tree)
	if "literal" in tree: return tree["literal"]

	return f"({create_z3(tree['left'])}) {tree['operator']} ({create_z3(tree['right'])})"

solve(eval(create_z3(get_tree_z3("root"))))
