#!/usr/bin/env python
# _*_ coding: utf-8 _*_ 
# vim^fileencoding=utf-8
import math

print("Введите номер задания:\n1.Решето Эратосфена\n2.Факторизация чисел\n3.Алгоритм Евклида бинарный\n4.Функция Эйлера")
ans = int(input())
if ans==1:
	print("Решето Эратосфена\nВведите число n: ")
	n = int(input())
	arr = set(range(2, n+1))
	while arr:
		prime = min(arr)
		print(prime, end = "\t")
		arr -= set(range(prime, n+1, prime))
elif ans==2:
	print("Факторизация числа\nВведите число n: ")
	n = int(input())
	i = 2
	arr = []
	while (i ** 2) <= n:
		while (n % i) == 0:
			arr.append(i)
			n = n / i
		i = i + 1
	if n > 1:
		arr.append(n)
	print(arr)
elif ans==3:
	print("Алгоритм Евклида бинарный\n")
	a = int(input("a = "))
	b = int(input("b = "))
	k=1
	while ((a!=0)&(b!=0)):
		while ((a%2==0)&(b%2==0)):
			a/=2
			b/=2
			k*=2
		while(a%2==0):
			a/=2
		while(b%2==0):
			b/=2
		if(a>=b):
			a-=b
		else:
			b-=a
	print(b*k)
elif ans==4:
	print("Функция Эйлера\nВведите число n: ")
	n = int(input())
	res = n
	en = int(math.sqrt(n)) + 1
	for i in range(2,en):
		if (n % i) == 0:
			while (n % i) == 0:
				n //= i
			res -= (res // i)
	if n > 1:
		res -= (res // n)
	print(res)
else:
	print("Неверный номер\n")
