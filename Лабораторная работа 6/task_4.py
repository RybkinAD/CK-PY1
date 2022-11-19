import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimeter=',', new_line='\n') -> list[dict]:
    with open(filename, 'r') as f:
        read_list = f.read().split()
        header_list = read_list[0].split(delimeter)
        data = read_list[1:]
        data_list = []
        for i in data:
            data_list.append(list(data[data.index(i)].split(delimeter)))
        list_dict = []
        for j in range(len(data_list)):
            each_dict = {}
            list_dict.append(each_dict)
            for k in range(len(header_list)):
                each_dict[header_list[k]] = data_list[j][k]
        return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
