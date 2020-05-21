digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list = []
for a in range (1,100):
    for b in range (100, 4999):
        d = str(a)+str(b)+str(a*b)
        if len(d)==9:
            count = 0
            for i in digits:
                if i in d:
                    count += 1
                    if count == 9:
                        list.append([a,b,a*b])
                else:
                    break

list_sum_product = []
for i in list:
    if i[2] not in list_sum_product:
        list_sum_product.append(i[2])

print(sum(list_sum_product))
