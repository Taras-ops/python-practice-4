def checkWordOrder(word, symbol, nextSymbol):
    if len(symbol) != 1 or len(nextSymbol) != 1:
        print('You should enter only a symbol')
        return False

    if symbol not in word or nextSymbol not in word:
        return False

    if word.index(nextSymbol) - word.index(symbol) != 1:
        return False

    return True


word = input('Enter a word: ')
symbol = input('Enter a symbol: ')
nextSymbol = input('Enter a next symbol: ')

print(checkWordOrder(word, symbol, nextSymbol))