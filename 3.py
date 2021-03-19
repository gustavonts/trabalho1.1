n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))

print('qual o tipo de conta?')
Opcao = int(input('1 - adição\ 2 - subtração\ 3 - multiplicação\ 4 - divisão'))

if Opcao == 1:
    Resultado = n1 + n2
elif Opcao == 2:
    Resultado = n1 - n2
elif Opcao == 3:
    Resultado = n1 * n2
elif Opcao == 4:
    Resultado = n1 / n2

print('Resultado = ', Resultado)

if Resultado % 2 == 0:
    print('número par')
else:
    print('número impar')

if Resultado >= 0:
    print('número positivo')
else:
    print('número negativo')

if Resultado == round(Resultado):
    print('número inteiro')
else:
    print('número decimal')
