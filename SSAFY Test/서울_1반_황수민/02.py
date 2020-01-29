def q2(word):
    count = 0
    for w in word:
        if w in 'aeiou':
            count += 1
    return count

print(q2('hello'))
print(q2('internationalization'))
print(q2('ssafy'))

