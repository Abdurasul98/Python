"""lambda, map, filter"""
word = input("Soz: ").split()


lenght = map(lambda words: len(words),word)
result = filter(lambda x: x >= 5,lenght)

print(list(result))