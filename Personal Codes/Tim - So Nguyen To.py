from array import *

print("Kiem tra mot so: 1")
print("Kiem tra mot day: 2")

you = float (input())

if you == 2:
	i = int

	i = 1

	A = array("i", [0])
	n =  int (input("Nhap so phan tu: "))

	print("Nhap cac so tu nhien: ")
	
	while (i <= n):
		A.extend([int (input())])

		i = i + 1

	i = 1

	print("----------")

	while (i <= n):	
		if A[i] != 2 and A[i] != 3:
			if A[i] %2 != 0:
				if A[i] %3 != 0:
					print(str(A[i]) + " la so nguyen to")

		else:
			print(str(A[i]) + " la so nguyen to")

		i = i + 1

elif you == 1:
	n = int (input("Nhap mot so tu nhien bat ki: "))

	if n == 2 or 3:
		print(str(n) + " la so nguyen to")

	elif n != 2:
		if n %2 != 0:
			if n %3 != 0:
				print(str(n) + " la so nguyen to")

else:
	print("Loi! Ban hay nhap lai")
