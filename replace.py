import sys

if len(sys.argv[2]) >= 2:
	goingTo = sys.argv[2]
else:
	goingTo = "out.txt"

with open(goingTo, "wt") as fout:
	with open(sys.argv[1], "rt") as fin:
		for line in fin:
			fout.write(line.replace("\n", ","))


