## 06. 集合

def n_gram(target, n):

    result = []
    for i in range(0, len(target) - n + 1):
        result.append(target[i:i + n])

    return result

print('06. 集合')
set_x = set(n_gram('paraparaparadise', 2))
print('A: ' + str(set_x))

set_y = set(n_gram('paragraph', 2))
print('B: ' + str(set_y))

set_or = set.union(set_x, set_y)
print('和集合: ' + str(set_or))
set_and = set_x & set_y # can also use set.intersection
print('積集合: ' + str(set_and))
set_minus = set_x - set_y # set.difference
print('差集合: ' + str(set_minus))

print('se in X? ' + str('se' in set_x))
print('se in Y? ' + str('se' in set_y))