data = []
with open('dane_1.txt') as file:
	for i in file:
		data.append(int(i))

counter = 0

#tab = [1, 2, 3, 2, 0, 4, 0, 1]
tab_sums = []

for i in range(len(data)):
	if i == len(data) - 2:
		break

	sum = 0

	for j in range(i, i + 3):
		sum += data[j]

	tab_sums.append(sum)

	print("suma: {}".format(sum))

for i in range(1, len(tab_sums)):
	if tab_sums[i] > tab_sums[i - 1]:
		counter += 1
		
print(counter)
#sum(data[i:3])