a_dictionary = {}
sum_dic = {}
myfile = open("inputone.txt", "r")
myline = myfile.readline()
print(myline)
i = 1
for line in myfile:
    if not line.strip() == "":
        a_dictionary.setdefault(i, []).append(int(line))
    else:
        i = i + 1
myfile.close()
total = len(a_dictionary)

o = 0
while total > 0:
    print(total)
    o = o + 1
    sum_dic[o] = sum(a_dictionary[o])
    total = total - 1
max_value = max(sum_dic.values())
print(max_value)




#total = sum(a_dictionary[].values())



""""
with open("inputone.txt") as f:

    for line in f:
        value = line.split() #Read every line
        print(value)
        print(type(value))
        exit()
        if not int(value): #When value is None
            i = i + 1
            print(i)
        else:
            a_dictionary[i] = value


print(a_dictionary)
"""
#Readline text file into dictionary
#detect when newline is empy new keyvalue to add values
#for each key create sum of all values

"""
for line in lines:
        if line.strip() == "":
            print('The line is empty')
"""