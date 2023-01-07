def count_info(data_dict, info):
    count = 0
    for e in range(1, len(data_dict)+1):
        for el in range(len(data_dict[e])):
            if data_dict[e][el] == info:
                count += 1
    return count


def find_info(data_dict, info):
    for value in data_dict.values():
        for el in value:
            if el == info:
                return value


def del_info(data_dict, info):
    for key, value in data_dict.items():
        if info in value:
            data_dict.pop(key)
            return data_dict


def search_data(data_dict, info):
    c = count_info(data_dict, info)
    if c == 0:
        return
    elif c == 1:
        return [find_info(data_dict, info)]
    elif c >= 2:
        res = []
        while c:
            res.append(find_info(data_dict, info))
            del_info(data_dict, info)
            c -= 1
        return res


def change_data(data_dict, element, num, new_info):
    for key, value in data_dict.items():
        if element == [value] or element == value:
            if num == 1:
                data_dict[key] = [new_info, value[1], value[2], value[3]]
            elif num == 2:
                data_dict[key] = [value[0], new_info, value[2], value[3]]
            elif num == 3:
                data_dict[key] = [value[0], value[1], new_info, value[3]]
            else:
                data_dict[key] = [value[0], value[1], value[2], new_info]
            return data_dict
