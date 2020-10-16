"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys
from collections import defaultdict


def read_file(filename):
    with open(filename) as file:
        return file.read().lower()


def make_list(filename):
    text = read_file(filename)
    text = text.split()
    dictionary = defaultdict(int)
    list = []
    for k in text:
        dictionary[k] += 1
    for c in dictionary.keys():
        list.append(c)

    return list


def make_dictionary(filename):
    text = make_list(filename)
    words = read_file(filename)
    words = words.split()
    dictionary = {}
    list = []
    cont = 0

    for c in text:
        for i, t in enumerate(words):
            if words[0] == c:
                dictionary[''] = [c]
            if c == t:
                if i + 1 < len(words):
                    cont = i + 1
                else:
                    cont = i
                if c == words[cont]:
                    list.append('')
                else:
                    list.append(words[cont])
        dictionary[c] = list.copy()
        list.clear()

    return dictionary


def mimic_dict(filename):
  """Retorna o dicionario imitador mapeando cada palavra para a lista de
  palavras subsequentes."""
  return make_dictionary(filename)


def print_mimic(mimic_dict, word):
  """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
  # +++ SUA SOLUÇÃO +++
  text = ''
  cont = 0
  pula = 20
  word = word
  for c in mimic_dict:
       word = random.choice(mimic_dict[word])
       text += ' ' + word
       cont += 1
       if cont == 200:
           break
       if '.' in word:
           text += '\n'
       elif cont == pula:
           pula += 20
  print(text)
  return text



# Chama mimic_dict() e print_mimic()
def main():
  if len(sys.argv) != 2:
    print('Utilização: ./14_mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
