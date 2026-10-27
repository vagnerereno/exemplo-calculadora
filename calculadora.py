# Crie uma calculadora em Python utilizando Programação Orientada a Objetos (POO)
# que realize as operações básicas de uma calculadora. Dicas:

# Defina uma classe com diversas funções, uma para cada tipo de operação (+, -, /, *);
class Calculadora:

    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

    def dividir(self, x, y):
        if y == 0:
            return "Erro: Divisão por zero."
        return x / y

    def multiplicar(self, x, y):
        return x * y