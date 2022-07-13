# Class 2 second - Home assignment - Q2 : part "a"
lst1 = [11, 7, 5, 8, 8, 17]
lst2 = [22, 8, 10, 11, 11]
lst3 = [71, 3, 2, 8, 2, 14, 1]
list_of_none_dup = []
dup_numbers = ""
dup_items = {}
new_lst = []
none_dup_lst_name = ""
dict_of_lists = {"lst1": lst1, "lst2": lst2, "lst3": lst3}
for key in dict_of_lists:
    # using sets to find witch list contain dup items and prints the list name and the witch values
    if len(set(dict_of_lists[key])) < len(dict_of_lists[key]):
        for value in dict_of_lists[key]:
            if dict_of_lists[key].count(value) > 1 and str(value) not in dup_numbers:
                dup_numbers += str(value) + " and "
    dup_items[key] = (dup_numbers[0:-5:1])
    dup_numbers = ""
for keys in dup_items.keys():
    if dup_items[keys] != "":
        print(keys, "- includes the values "+dup_items[keys], "more than once")
    else:
        none_dup_lst_name += keys + " and "
        list_of_none_dup += dict_of_lists[keys]
# Class 2 second - home assignment - Q2 : part "b"
for end_number in list_of_none_dup:
    if list_of_none_dup.count(end_number) > 1 and end_number not in new_lst:
        new_lst.append(end_number)
if len(new_lst) == 0:
    if none_dup_lst_name == "":
        print(None)
    else:
        print("values of("+none_dup_lst_name[0:-5:1] + ") are", dict_of_lists[none_dup_lst_name[0:-5:1]])
else:
    print("common values of("+none_dup_lst_name + ") are", new_lst)
