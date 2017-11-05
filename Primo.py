def primo(num):
	if num<2:
		return "No es un numero primo"
	else:
		for i in range(2, num):
			if num%i==0:
				return "No es un numero primo."
			else:
				return "Si es un numero primo."
a=int(input("Numero= "))
print(primo(a))