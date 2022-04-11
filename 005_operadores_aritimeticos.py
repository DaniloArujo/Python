# + adição, - subtração, * multiplicação, / divisão,
# ** potencia, // divisão inteira, % resto da divisão.


x = int(input("Digite um numero: "))
y = int(input("Digite um outro numero: "))

s = x + y
m = x * y
d = x / y
di = x // y
e = x ** y
rd = x % y
ra = x ** ( 1/2 )

print(f"A soma é {s}, a multiplicação é {m}, a divisão é {d} "
      f"a divisão inteira é {di}, a exponenciação é {e} e "
      f"o resto da divisão é {rd}, a raiz de x é {ra}.")
