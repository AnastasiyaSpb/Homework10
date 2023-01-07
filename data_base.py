import pathlib
from pathlib import Path


def add_data(new_data):
    data = Path("data.txt")
    with open(data, "a", encoding='utf-8') as current_data:
        current_data.writelines(new_data + "\n")


def show_data():
    data = Path("data.txt")
    f = open(data, "r", encoding='utf-8')
    if f == None:
        print("Справочник пуст")
    else:
        for line in f:
            print(line, end="")
    f.close()


def create_dict():
    data = Path("data.txt")
    data_dict = {}
    with open(data, "r", encoding='utf-8') as file:
        data_list = list(map(lambda x: x.replace("\n", ""), file.readlines()))
        key_data = 1
        arg = 4          # количество описаний одной записи
        for e in range(arg-1, len(data_list), arg+1):
            data_dict[key_data] = [data_list[e-3],
                                   data_list[e-2], data_list[e-1], data_list[e]]
            key_data += 1
    return data_dict

def create_dict_csv():
    data = Path("data.txt")
    data_dict = {}
    with open(data, "r") as file:
        data_list = list(map(lambda x: x.replace("\n", ""), file.readlines()))
        familia_list = []
        name_list = []
        phone_list = []
        comnt_list = []
        for i in range(0,len(data_list),5):
            familia_list.append(data_list[i])
        data_dict["Фамилия"] = familia_list
        for i in range(1,len(data_list),5):
            name_list.append(data_list[i])
        data_dict["Имя"] = name_list
        for i in range(2,len(data_list),5):
            phone_list.append(data_list[i])
        data_dict["Номер телефона"] = phone_list
        for i in range(3,len(data_list),5):
            comnt_list.append(data_list[i])
        data_dict["Комментарий"] = comnt_list
    return data_dict


def unpack_dict(data_dict):
    data = Path("data.txt")
    if data == None:
        return None
    else:
        with open(data, "w", encoding='utf-8') as file:
            for value in data_dict.values():
                file.writelines(
                    f"{value[0]}\n{value[1]}\n{value[2]}\n{value[3]}\n\n")

# def csv_format (data_dict):
#     data = Path("data_new.txt")
#     with open(data, "w", encoding='utf-8') as file:
#         for value in data_dict.values():
#             file.writelines(
#                 f"{value[0]}; {value[1]}; {value[2]}; {value[3]}\n")