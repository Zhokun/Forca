# from random import choice
#
# palavras = ["banana", "carro", "morango", "sofa", "carruagem", "casa"]
#
# palavra = choice(palavras)
#
# print(f"A palavra escolhida foi {palavra}")
# palavra_escondida = list("_" * len(palavra))
#
#
# while "_" in palavra_escondida:
#     print(f"{''.join(palavra_escondida)}")
#     letra = input("Escolha uma letra")
#     for index, l in enumerate(palavra):
#         if letra == l:
#             palavra_escondida[index] = letra
# else:
#     print(f"Parabéns,você acertou a palavra {''.join(palavra_escondida).upper()}")
#
import string

print(string.ascii_lowercase)