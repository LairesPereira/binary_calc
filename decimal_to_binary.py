def translate_dec_to_bin(decimalNumber):
    number = decimalNumber
    bin_result = []
    while number > 0:
        # print(int(number % 2))
        bin_result.append(int(number % 2))
        number = number // 2
        print(f'number: {number}, list: {bin_result}')

translate_dec_to_bin(1250)