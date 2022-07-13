def main(): 

    # matriz que guarda os dados {nome} e {faturamento mensal}
    monthlySales = [["SP", 67836.43] , ["RJ", 36678.66], ["MG", 29229.88], ["ES", 27165.48], ["Outros", 19849.53]]
    sumOfSales = 0

    aux = len(monthlySales)
    
    for i in range(aux): # loop que realiza a soma do faturamento
        sumOfSales += monthlySales[i][1]

    for i in range(aux): # impressão dos rsultados
        proportionOfSale = (monthlySales[i][1] / sumOfSales) * 100
        print(f"O percentual de(o) {monthlySales[i][0]} no valor total R${sumOfSales: .2f} é de: {proportionOfSale: .2f}%")
    print()

main()