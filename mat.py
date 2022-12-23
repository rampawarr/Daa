# Importing Module
from bisect import bisect_right as upper_bound

# Function To Find Median In The matrix
def binaryMedian( matrix , r , c ):
	min = matrix[0][0]
	max = 0

	for i in range(r):
		if matrix[i][0] < min:
			min = matrix[i][0]
		if matrix[i][c-1] > max :
			max = matrix[i][c-1]

	desired = (r * c + 1) // 2

	while (min < max):
		mid = min + (max - min) // 2
		place = [0];
		for i in range(r):
			j = upper_bound(matrix[i], mid)
			place[0] = place[0] + j
		if place[0] < desired:
			min = mid + 1
		else:
			max = mid
	print ("Median is : ", min)
	return

# Input Of The matrix
r = int(input("Enter no.of rows : "))
c = int(input("Enter no.of columns : "))
print("Enter the elements of the matrix : ")
matrix = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
binaryMedian( matrix , r , c )