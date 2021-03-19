combustivel = str(input("Digite o tipo de combustível:"))
litro = float(input("Digite a quantidade de litros:"))

if combustivel == "alcool":
    alcool = 3.5
    custo = litro * alcool
    if litro <= 20:
        desconto1 = (custo * 3)/100
        print(f"O desconto de combustível foi de : {desconto1} e o preço agora é {custo-desconto1}")
    elif litro > 20:
        desconto2 = (custo * 5)/100
        print(f"O desconto de combustível foi de : {desconto2} e o preço agora é {custo-desconto2}")

elif combustivel == "gasolina":
    gasolina = 4.6
    custo = litro * gasolina
    if litro <= 20:
        desconto3 = (custo * 4)/100
        print(f"O desconto de combustível foi de : {desconto3} e o preço agora é {custo-desconto3}")
    elif litro > 20:
        desconto4 = (custo * 6)/100
        print(f"O desconto de combustível foi de : {desconto4} e o preço agora é {custo-desconto4}")