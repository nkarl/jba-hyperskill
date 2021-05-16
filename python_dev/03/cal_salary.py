with open('salary.txt') as in_f, \
     open('salary_year.txt', 'w') as out_f:
    s = in_f.readlines()
    for p in s:
        p = p.strip()
        out_f.write(f'{int(p) * 12}\n')
