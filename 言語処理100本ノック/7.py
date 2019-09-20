## 07. テンプレートによる文生成
# def templete(x, y, z):
#     return str(x) + '時の' + y + 'は' + str(z)


# result = templete(12, '気温', 22.4)
def templete(x, y ,z):
    return '{}時の{}は{}'.format(x, y, z)

print('07. テンプレートによる文生成')
print(templete(12, '気温', 22.4))