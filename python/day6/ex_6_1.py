infile = "files/dane_6.txt"
X = [int(x) for x in open(infile).read().split(",")]
print(X)