from binary_calc import translate_binary

while True:
    tool_choice = int(input('Digite 1 se deseja traduzir ou 2 se deseja somar: '))
    if(tool_choice != 1 and tool_choice != 2):
        print('Entrada inválida, seu puto!!!')
    elif(tool_choice == 1):
        print(translate_binary(input('Digite um número para traduzir: ' )))
        break
    else:
        first_binary_translated = translate_binary(input('Digite o primeiro binario: '))
        second_binary_translated = translate_binary(input('Digite o segundo binário: '))
        print(f'A soma dos binários é: {int(first_binary_translated) + int(second_binary_translated)}')
        break


