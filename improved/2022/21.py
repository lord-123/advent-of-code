from util import *
import operator

ws = readlineswords("21.in")

ins = { w[0][:-1]: list(w[1:]) for w in ws }

def get_tree(start):
	if len(ins[start]) == 1:
		return { "literal": eval(ins[start][0]) }

	return { "operator": OPS[ins[start][1]],
			 "args": (get_tree(ins[start][0]), get_tree(ins[start][2])) }

# p1
print("p1", int(eval_tree(get_tree("root"))))

# p2
humn = Int("humn")
ins["root"][1] = "=="
ins["humn"] = ["humn"]
s = Solver()
s.add(eval_tree(get_tree("root")))
s.check()

print("p2", s.model()[humn])
