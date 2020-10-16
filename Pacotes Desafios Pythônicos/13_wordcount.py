"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys
from operator import itemgetter, attrgetter

def le_arquivo(filename):
    with open(filename) as file:
        return file.readlines()

def prepara_texto(filename):
    texto = le_arquivo(filename)
    letras = []
    exclui = [' ', '\n']
    for c in texto:
        for letra in c:
            if letra not in exclui:
                letras.append(letra.lower())

    return letras


def conta_letras(filename):
    texto = prepara_texto(filename)
    dic = {}

    for c in texto:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1

    return dic


def print_words(filename):
    texto = conta_letras(filename)
    texto = sorted(texto.items(), key=itemgetter(0))

    for c in texto:
        print(c[0], c[1])

    return


def print_top(filename):
    texto = conta_letras(filename)
    texto = sorted(texto.items(), key=itemgetter(1), reverse=True)
    cont = 0

    for c in texto:
        if cont < 20:
            print(c[0], c[1])
        cont += 1
    return


def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
