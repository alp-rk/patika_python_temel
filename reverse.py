#Verilen liste içindeki elemanları tersine çeviren,
#elemanları listeyse onlarıda tersine çeviren program
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = []

def f(liste):
    liste.reverse()
    for i in liste:
        if type(i)==list:
            i.reverse()
            output_list.append(i)
        else:
            output_list.append(i)

f(input_list)
print(output_list)