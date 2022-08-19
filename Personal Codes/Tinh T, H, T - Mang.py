#Mang nhap tu ban phim
from array import *

i = 1
tong = hieu = float (0)
tich = float (1)

A = array('d', [0])
n = int (input("Nhap so phan tu: "))

print("Ban hay nhap cac so: ")

while (i <= n):	
	A.extend([float (input())])

	tong = tong + A[i]
	hieu = hieu - A[i]
	tich = tich * A[i]

	i = i + 1

print("Ban muon tinh tong, hieu hay tich cua mang?")
print('Neu ban muon tinh all, nhap: "tong and hieu and tich"')
you = input()
if you == "tong":
	print(tong)

elif you == "hieu":
	print(hieu)

elif you == "tich":
	print(tich)

elif you == "tong and hieu and tich":
	print(tong)
	print(hieu)
	print(tich)

else:
	print('Ban chi co the chon "tong", "hieu", "tich" hoac "tong and hieu and tich"')
