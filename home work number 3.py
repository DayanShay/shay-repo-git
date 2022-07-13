def print_values_above(check_dict_above_age: dict, age_check=0) -> None:
    """
    function gets two parameters ,1 a dictionary,2 age (optional).
    if got number (age_check)- prints all values above age_check, else prints check_dict_above_age
    :param check_dict_above_age: dictionary example - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
    :param age_check: int but can be anything
    :return:None
    """
    if str(age_check).isnumeric():
        for dict_id in dict(check_dict_above_age).keys():
            if int(check_dict_above_age[dict_id]["age"]) > int(age_check):
                print({dict_id: check_dict_above_age[dict_id]})
    else:
        print(check_dict_above_age)


def find_median_average(check_dict: dict) -> dict[int, int]:
    """function gets a dictionary like - > {3322117: {"name": "Tal", "sex": "male", "age": 22} and ect
    and returns the average age ,and the median of all ages in dictionary
    :param check_dict: dictionary example - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
    :return: avg_age = the average age , mid_age =  median of all ages
    """
    n = len(check_dict)
    if n == 0:
        return 0, 0
    else:
        age_list = []
        for dict_id in dict(check_dict).keys():
            age_list.append(check_dict[dict_id]["age"])
        avg_age = "%.f" % (sum(age_list) / n)
        age_list.sort()
        if n % 2 == 1:
            return avg_age, age_list[n // 2]
        else:
            index = n // 2
            mid_age = "%.f" % ((age_list[index - 1] + age_list[index]) / 2)
        return avg_age, mid_age


def split_male_female(data_set_check: dict) -> tuple[dict, dict]:
    """
    function gets a dictionary like - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
    and create and returns a dictionary for each gender male = male_part and  female = female_part
    :param data_set_check: dictionary example - > {3322117: {"name": "Tal", "sex": "male", "age": 22}
    :return:  male_dict , female_dict
    """
    female_dict = {}
    male_dict = {}
    for dict_id in dict(data_set_check).keys():
        if data_set_check[dict_id]["sex"] == "female":
            female_dict[dict_id] = data_set_check[dict_id]
        else:
            male_dict[dict_id] = data_set_check[dict_id]
    return male_dict, female_dict


def main():
    data_set = {176864201: {"sex": "male", "age": 27, "height": 1.55, "name": "sean"},
                17686231: {"sex": "male", "age": 32, "height": 1.73, "name": "dan"},
                17627431: {"sex": "male", "age": 44, "height": 1.68, "name": "arthur"},
                176864301: {"sex": "female", "age": 57, "height": 1.55, "name": "Anat"},
                17686431: {"sex": "female", "age": 82, "height": 1.73, "name": "danna"},
                17687431: {"sex": "female", "age": 27, "height": 1.68, "name": "amy"}}
    male_part, female_part = split_male_female(data_set)
    avg_age_males, mid_age_males, avg_age_females, mid_age_females = find_median_average(male_part) + find_median_average(female_part)
    print_values_above(data_set, age_check=input("insert age : (not must)"))
    print("average age males", avg_age_males, "\n" + "mid age for males", mid_age_males, "\n" + "average age females",
          avg_age_females, "\n" + "mid age for females", mid_age_females)
    avg_all, mid_all = find_median_average(data_set)
    print("average age all", avg_all + "\n" + "mid age all", mid_all)


if __name__ == "__main__":
    main()
