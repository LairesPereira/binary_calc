numbers_list = []

    # number list deve sempre ser uma string somente com 1 ou 0
def translate_binary(numbersList): 
    # recebe uma string de numeros e joga em uma lista
    for number in numbersList:
        numbers_list.append(number)

    # as potencias são iguais ao tamanho da lista -1 para que a ultima potencia seja zero
    power = len(numbers_list) - 1
    
    final_sum = 0 
    for number in numbers_list:
        # calculamos a potencia somente se o valor for de um bit ligado
        print(f'number: {number} power: {power}')
        if(int(number) == 1):
            final_sum += 2**power
        power -= 1 #sempre diminuimos o valor da potencia para a proxima iteracao

    print(f'soma: ', {final_sum})
    numbers_list.clear()
    return(final_sum)

