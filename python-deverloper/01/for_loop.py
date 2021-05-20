s1 = 'python'
s2 = 'CamelCase'
s3 = 'lowerCamelCase'
s4 = 'LowerCamelCase'

def snake_it(input):
    s = input
    e = ''
    for i in range(len(s)):
        c = s[i]
        if not c.islower():
            if i == 0:
                e += c.lower()
            else:
                e += '_' + c.lower()
        else:
            e += c
    return e

res1 = snake_it(s1)
res2 = snake_it(s2)
res3 = snake_it(s3)
res4 = snake_it(s4)
print()
