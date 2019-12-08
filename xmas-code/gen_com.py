import copy

g_list = [0,1,2,3,4]

def get_all_combinations(element_list):
    out_list = []
    if len(element_list) > 1:
        sub_list = get_all_combinations(element_list[1:])

        for x in sub_list:
            out_list = out_list + create_comb_set(element_list[0], x)

        return out_list
    else:
        return [element_list]


def create_comb_set(n, li):
    output = []
    for i in range(0, len(li) + 1):
        temp = copy.copy(li)
        temp.insert(i, n)
        output.append(temp)

    return output

print(get_all_combinations(g_list))