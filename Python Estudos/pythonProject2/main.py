str_list = ['João', 'Roberto', 'Rafael']

for name in str_list:
    for c in name:
        if c in 'aeiou':
            print(c)
