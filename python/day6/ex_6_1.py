infile = "dane_6.txt"
X = [int(x) for x in open(infile, "rb").read().split(",")]

tmp = 0

for i in range(80): # 0 - 18
	#print("Initial state: {}".format(X)) if i == 0 else print("After {} days: {}".format(i, X))
	for j, item in enumerate(X):
		if X[j] == 0:
			X[j] = 7
			tmp += 1
	X[:] = [number - 1 for number in X]
	while tmp is not 0:
		X.append(8)
		tmp -= 1

print(len(X))