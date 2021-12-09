from sys import maxsize


with open("files/dane_7.txt", "r") as f:
   lines = f.readline()


data = [int(num) for num in lines.split(",")] 

def calc_cost(tab, currentShift = 0, minValue = min(data), maxValue = max(data)):
	min_sum = maxsize
	for i in range(minValue, maxValue, 1):
		sum = 0
		currentCost = minValue + i
		for j in range(len(tab)):
			distance = abs(tab[j] - currentCost)
			sum += distance * (distance + 1) / 2
		if sum < min_sum:
			min_sum = sum
		#print(int(sum))
	print(int(min_sum))

calc_cost(data)