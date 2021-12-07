from sys import maxsize

with open("files/dane_7.txt", "r") as f:
   lines = f.readline()


data = [int(num) for num in lines.split(",")]
min_sum = maxsize



for i in range(min(data), max(data)):
	sum = 0
	minValue = min(data) + i
	for j in range(len(data)):
		sum += abs(data[j] - minValue)
	if sum < min_sum:
		min_sum = sum

print(min_sum)

