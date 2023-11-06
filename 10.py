def C_A(salario):
    abono = max(0.2 * salario, 100)
    return abono

funcionarios = 0
abono_total = 0

while True:
    salario = float(input("Digite o salário (ou 0 para encerrar): "))
    if salario == 0:
        break

    abono = C_A(salario)
    funcionarios += 1

    print(f"Salário: R${salario:.2f} | Abono: R${abono:.2f}")

print(f"Total de funcionários processados: {funcionarios}")
print(f"Total a ser gasto com o abono: R${gasto_abono:.2f}")