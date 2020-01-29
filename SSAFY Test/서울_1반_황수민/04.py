def q4(word):
    result = {}
    for w in word:
        if w not in result.keys():
            result[w] = 1
        else:
            result[w] += 1
    return result

print(q4('hello'))
print(q4('internationalization'))
print(q4('haha'))