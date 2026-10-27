# Defina uma classe principal na qual o usuário vai poder interagir com a calculadora.
# Dependendo do comando do usuário, a calculadora realiza a operação correspondente.
from calculadora import Calculadora

if __name__ == "__main__":

    calculadora = Calculadora()

    while True:
        print("\n Operações disponíveis: somar, subtrair, dividir ou multiplicar.")

        operacao = input("Escolha a operação ou digite 'sair' para encerrar a calculadora: ").strip().lower()

        if operacao == 'sair':
            print("A calculadora foi encerrada.")
            break

        numero_1 = float(input("Digite o primeiro número: "))
        numero_2 = float(input("Digite o segundo número: "))

        if operacao == 'somar':
            resultado = calculadora.somar(numero_1, numero_2)
        elif operacao == 'subtrair':
            resultado = calculadora.subtrair(numero_1, numero_2)
        elif operacao == 'dividir':
            resultado = calculadora.dividir(numero_1, numero_2)
        elif operacao == 'multiplicar':
            resultado = calculadora.multiplicar(numero_1, numero_2)
        else:
            print("Operação inválida. Tente novamente.")

        with open("log.txt", "a", encoding="utf-8") as log:
            log.write("O usuário escolheu a opção: " +
                      operacao + " e o resultado foi: "
                      + str(resultado) + "\n")

        print("O resultado da operação é: ", resultado)

        print("Alteração nova!!!!!")