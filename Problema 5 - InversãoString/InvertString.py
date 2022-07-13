# Função que fará a inversão da string
def invert(string) -> str:
    return string[::-1]

# Função de execução
def main():
    inputString = input("Digite a string desejada: ")
    inputReverse = invert(inputString)
    print(inputReverse)
main()