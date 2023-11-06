impar = 0
pares = 0


for i in range(10):
    numero = int(input(f'Digite o {i+1}º número: '))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impar += 1
        
print(f'Quantidade de números impares: {impar}')
print(f'Quantidade de números pares: {pares}')