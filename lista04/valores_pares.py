# Antonio Claudio Teixeira Alves

# Faça um programa que leia um número inteiro positivo par N e
# imprima todos os números pares de 0 até N em ordem crescente

def separador():
    print("-"*25)

separador()
print("Contador de números pares")
separador()

number_pair = int(input("Digite um valor par: "))

if number_pair % 2 == 0:
    for i in range(0, number_pair+1, 2):
        print(i, end=" ")
else:
    print("[ERRO] número inválido")
