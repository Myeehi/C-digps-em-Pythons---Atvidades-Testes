a = int(input("Escolha: 1 - Feminino / 2 - Masculino"))
h = float(input("Informe a sua altura"))

if a == 1:
    p= (62.1*h)-44.7
    print("O seu peso ideal é" , p , "kg")
else:
    p= (72.7*h)-58
    print("O seu peso ideal é" ,p, "kg")    