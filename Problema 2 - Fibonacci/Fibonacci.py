# Função fibonacci definida recursivamente
def fibonacciFunction(n):
    if n <= 1: 
        return n
    return fibonacciFunction(n-1) + fibonacciFunction(n-2)

# Função que cria a sequência de fibonacci
def handleCreateList():
    listOfNumbers = []
    # range definido de forma estática, que cria a sequência
    for i in range(10): 
        listOfNumbers.append(fibonacciFunction(i))
    return listOfNumbers

# Função que verifica se os números estão contidos na sequência
def numberInList(number):
    resultList = handleCreateList()
    print(resultList)
    if number in resultList:  
        print(f"O número {number} está na sequência de fibonacci")
    else: 
        print(f"O número {number} não está na sequência de fibonacci")

# Função de execução
def main() -> str:
    number = int(input("Digite um número: "))
    numberInList(number)
main()



