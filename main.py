import re


def first_unic_symbol(input_text):
    if type(input_text) != str:
        raise TypeError('Input_text variable must be string type')
    if len(input_text) == 0:
        raise ValueError('Entering an empty string')
    
    words = re.findall(r'\b\w+\b', input_text)

    symbols = []

    for word in words:
        for i in range(len(word)):
            if word.count(word[i]) == 1:
                symbols.append(word[i])
                break

    for symbol in symbols:
        if symbols.count(symbol) == 1:
            return symbol

    return 'No unique symbols'
