# Desafio: pedir o nome de um aluno e uma nota, gravar no arquivo notas.txt
# e depois ler o arquivo para exibir todas as notas cadastradas.


with open("notas.txt", "a") as arquivo:

    for i in range(5):
        nome = input("Por favor, digite o seu nome: ")
        nota = input("Agora digite a sua nota: ")

        arquivo.write(nome + " - " + nota + "\n")