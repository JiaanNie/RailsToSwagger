def Convert(routes_list):
    result = [] # array of dict
    for list in routes_list:
        d = {}
        for i in range(3):
            if i == 0:
                d["url"]= list[i]
            elif i == 1:
                d["method"] = list[i].lower()
            else:
                list[-1] = list[-1][:list[-1].find('\n')]
                d["purpose"]=' '.join(list[2:])
        result.append(d)
    return result
