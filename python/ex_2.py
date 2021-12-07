depth = 0
horizontal = 0
aim = 0

with open('dane_2.txt') as file:
    data = file.read().splitlines()

a, b = zip(*(s.split(" ") for s in data))

b = list(map(int, b))

for i in range(len(data)):
	if a[i] == 'forward':
		horizontal += b[i]
		depth += aim * b[i]
	elif a[i] == 'down':
		aim += b[i]
	elif a[i] == 'up':
		aim -= b[i]

print("horizontal {}, depth {}".format(horizontal, depth))
print(horizontal * depth)
#print(data)