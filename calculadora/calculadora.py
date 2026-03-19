import soma
import subtrai
import multiplica
import divide

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    resultado = soma.somaf(a, b)
elif op == "-":
    resultado = subtrai.subtraif(a, b)
elif op == "*":
    resultado = multiplica.multiplicaf(a, b)
elif op == "/":
    resultado = divide.dividef(a, b)
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)