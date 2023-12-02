with open("input", "r") as file:
	ll = file.read()[:-1].split("\n")

nums = {
	"2": 2,
	"1": 1,
	"0": 0,
	"-": -1,
	"=": -2,
	}

def snafu(x):
	s = 0
	while len(x) > 0:
		s *= 5
		s += nums[x[0]]
		x = x[1:]
	return s

def to_snafu(x):
	s = ""
	while x > 0:
		x, d = divmod(x+2, 5)
		s = "=-012"[d] + s
	return s

print(to_snafu(sum(snafu(x) for x in ll)))
