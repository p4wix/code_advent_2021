import numpy as np

def getCharList(str):
	return [char for char in str]

with open('dane_3.txt') as file:
   data = file.read().splitlines()

for i in range(len(data)):
	data[i] = getCharList(data[i])

l_2d_t = np.array(data).T.tolist()

cZeros = 0
cOnes = 0
gamma = ''
eps = ''

for i in range(len(l_2d_t)):
	cZeros = 0
	cOnes = 0
	for j in range(len(l_2d_t[i])):
		if l_2d_t[i][j] == '0':
			cZeros += 1
		else:
			cOnes += 1

	if cZeros > cOnes:
		gamma += "0"
		eps += "1"
	else:
		gamma += "1"
		eps += "0"
	print("Next: {} ".format(gamma))

print(int(gamma, 2))
print(int(eps, 2))

print(int(gamma, 2) * int(eps, 2))