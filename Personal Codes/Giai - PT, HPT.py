# Giai phuong trinh va he phuong trinh
import time

time.sleep(0.5)
# Cach chon phuong trinh, he phuong trinh --> giai/ ket thuc chuong trinh  
print('----------------------------------')
print('Alien: First degree equation one hidden: 1.1')
print('       System of two first degree equations with two unknowns: 1.2')
print('       System of three first order equations with three unknowns: 1.3')
print('       Quadratic equation one hidden: 2.1')
print('----------------------------------')
print('Alien: If you want to end, please type : end')

while True:
	time.sleep(0.5)
	you = input('You: ') # Nhap gia tri tuong ung

	time.sleep(0.5)
	if you == '1.1': # Phuong trinh bac nhat mot an
		print('Alien: You have chosen to first degree equation one hidden.')
		
		x = float

		time.sleep(0.5)
		a = float (input('Alien: Please enter real number a: '))
		time.sleep(0.5)
		b = float (input('Alien: Please enter real number b: '))

		time.sleep(0.5)
		if a == 0:
			if b == 0:
				print('Alien: Equation with infinite solutions.')
			else:
				print('Alien: Equation with no solution.')
		else:
			x = -b/a
			print('Alien: Equation has solution X = ',x)
	
	elif you == '1.2': # He hai phuong trinh bac nhat hai an
		time.sleep(0.5)
		print('Alien: You have chosen to system of two first degree equations with two unknowns.')

		time.sleep(0.5)
		a1 = float (input('Alien: Please enter real number a1: '))
		time.sleep(0.5)
		b1 = float (input('Alien: Please enter real number b1: '))
		time.sleep(0.5)
		c1 = float (input('Alien: Please enter real number c1: '))
		time.sleep(0.5)
		a2 = float (input('Alien: Please enter real number a2: '))
		time.sleep(0.5)
		b2 = float (input('Alien: Please enter real number b2: '))
		time.sleep(0.5)
		c2 = float (input('Alien: Please enter real number c2: '))

		if a1/a2 == b1/b2 == c1/c2:
			time.sleep(0.5)
			print('Alien: Equation with infinite solutions.')

		elif a1/a2 == b1/b2 != c1/c2:
			time.sleep(0.5)
			print('Alien: Equation with no solution.')

		else:
			x = y = float
			y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)
			x = (c1 - b1*y) / a1
			time.sleep(0.5)
			print('Alien: Equation has solution:')
			time.sleep(0.5)
			print('Alien: X = ',x)
			time.sleep(0.5)
			print('Alien: Y = ',y)
	
	elif you == '1.3': # He ba phuong trinh bac nhat ba an
		time.sleep(0.5)
		print('Alien: You have chosen to system of three first order equations with three unknowns.')

		x = y = z = float
		a1 = float (input('Alien: Please enter real number a1: '))
		time.sleep(0.5)
		b1 = float (input('Alien: Please enter real number b1: '))
		time.sleep(0.5)
		c1 = float (input('Alien: Please enter real number c1: '))
		time.sleep(0.5)
		d1 = float (input('Alien: Please enter real number d1: '))
		time.sleep(0.5)
		a2 = float (input('Alien: Please enter real number a2: '))
		time.sleep(0.5)
		b2 = float (input('Alien: Please enter real number b2: '))
		time.sleep(0.5)
		c2 = float (input('Alien: Please enter real number c2: '))
		time.sleep(0.5)
		d2 = float (input('Alien: Please enter real number d2: '))
		time.sleep(0.5)
		a3 = float (input('Alien: Please enter real number a3: '))
		time.sleep(0.5)
		b3 = float (input('Alien: Please enter real number b3: '))
		time.sleep(0.5)
		c3 = float (input('Alien: Please enter real number c3: '))
		time.sleep(0.5)
		d3 = float (input('Alien: Please enter real number d3: '))

		z = (
		((a1*b3 - a3*b1) * (a1*d2 - a2*d1) - 
		 (a1*d3 -a3*d1) * (a1*b2 - a2*b1)) 
		/ 
		((a1*b3 - a3*b1) * (a1*c2 - a2*c1) - 
		 (a1*c3 - a3*c1) * (a1*b2 - a2*b1)))
		y = ((a1*d2 - a2*d1) - (a1*c2 - a2*c1)*z) / (a1*b2 - a2*b1)
		x = (d1-b1*y - c1*z) / a1

		time.sleep(0.5)
		if a1/a2/a3 == b1/b2/b3 == c1/c2/c3 == d1/d2/d3:
			print('Alien: Equation with infinite solutions.')

		elif a1/a2/a3 == b1/b2/b3 == c1/c2/c3 != d1/d2/d3:
			print('Alien: Equation with no solution.')

		else:
			print('Alien: Equation has solution:')
			time.sleep(0.5)
			print('Alien: X = ',x)
			time.sleep(0.5)
			print('Alien: Y = ',y)
			time.sleep(0.5)
			print('Alien: Z = ',z)

	elif you == '2.1': # Phuong trinh bac ai mot an
		time.sleep(0.5)
		print('Alien: You have chosen to quadratic equation one hidden.')

		time.sleep(0.5)
		a = float (input('Alien: Please enter real number a: '))
		time.sleep(0.5)
		b = float (input('Alien: Please enter real number b: '))
		time.sleep(0.5)
		c = float (input('Alien: Please enter real number c: '))

		delta = b**2 - 4*a*c

		if delta < 0:
			time.sleep(0.5)
			print('Alien: Equation with no solution.')

		elif delta == 0:
			time.sleep(0.5)
			print('Alien: Equation with double solution equation with infinite solutions:')

			x = b / (2*a)

			time.sleep(0.5)
			print('Alien: X = ',x)

		else:
			time.sleep(0.5)
			print('Alien: Equation has two distinct solutions:')

			x1 = (-b + delta**(1/2)) / (2*a)
			x2 = (-b - delta**(1/2)) / (2*a)
			
			time.sleep(0.5)
			print('Alien: X1 = ',x1)
			print('Alien: X2 = ',x2)

	elif you == 'end': # Ket thuc chuong trinh
		time.sleep(0.5)
		print('Alien: See you!')
		
		time.sleep(1)
		break

	else: # Hien thi khi ban nhap mot gia tri ngoai gia tri da de xuat
		time.sleep(0.5)
		print('Alien: Error! Please re-enter.')
