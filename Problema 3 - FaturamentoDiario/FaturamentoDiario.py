import json

# Seja l a lista de valores

# Função que calcula o maior valor 
def biggerValue(l, lDay):
    bigger = max(l)
    i = l.index(bigger)
    return bigger, lDay[i]

# Função que calcula o menor valor 
def smallerValue(l, lDay):
    smaller = min(num for num in l if num != 0)
    i = l.index(smaller)
    return smaller, lDay[i]

# Função que calcula os dias em que
# o valor foi maior que a média 
def biggerSale(l):
    sum, aux, interval, numberOfDays = 0, 0, len(l), len(l)  

    for i in range(interval):
        sum += l[i] 

    for k in range(interval):
        if l[k] == 0:
            numberOfDays -= 1
        average = sum / numberOfDays
        if l[k] > average:
            aux += 1
    return aux


# Função de execução
def main():
    
    # consumindo o arquivo json e realizando o tratamento
    with open("Problema 3 - FaturamentoDiario/dados.json") as data: 
        dataOfSale = json.load(data)

    listOfData, listOfValues, listOfDays = [], [], []

    aux = len(dataOfSale)

    for i in range(aux):
        [listOfData.extend([v]) for v in dataOfSale[i].values()]
    
    for k in range(0, len(listOfData), 2):
        listOfDays.append(listOfData[k])

    for k in range(1, len(listOfData), 2):
        listOfValues.append(listOfData[k])

    smaller, smallerDay = smallerValue(listOfValues, listOfDays)
    bigger, biggerDay = biggerValue(listOfValues, listOfDays)

    print(f" O menor valor de faturamento foi R${smaller: .2f} no dia {smallerDay},\n", 
        f"enquanto o maior valor de faturamento foi R${bigger: .2f} no dia {biggerDay},\n",
        f"e a quantia de dias que ultrapassaram a média mensal foram {biggerSale(listOfValues)} dias.")

main()