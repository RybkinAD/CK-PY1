import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimeter=',') -> list[dict]:
    with open(filename, 'r') as f:
        header_list = f.readline().rstrip('\n').split(',')
        read_list = f.read().split()
        data_list = []
        for i in read_list:
            data_list.append(read_list[read_list.index(i)].split(delimeter))
        list_dict = [{header_list[j]: data_list[k][j] for j in range(len(header_list))}
                     for k in range(len(data_list))]
        return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
