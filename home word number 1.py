# Class 1 first - Home assignment - Q1 : part "a"
lst = [3, 7, 2]
histo = []
for item in lst:
    histo += [item*"*"]
print(histo)


# Class 1 first - Home assignment - Q1 : part "b"
first_list = [3, 7, 2]
second_list = [2, "b", "c"]
lst_res = []
for i in range(len(first_list)):
    lst_res.append(str(first_list[-i-1])+str(second_list[i]))
print(lst_res)

