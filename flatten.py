#Verilen listeyi düzleştiren flatten projesi
input_list=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list=[]
def flatten(x):
    for i in x:
        if type(i) == list:
            flatten(i)
        else:
            output_list.append(i)
flatten(input_list)
print(output_list)