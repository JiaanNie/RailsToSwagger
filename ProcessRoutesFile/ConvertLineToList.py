def Convert(routes_file):
    listArray = []
    for line in routes_file:
        line_list = line.split(' ')
        line_list = filter(None, line_list)
        listArray.append(line_list)
    listArray.sort()
    ## remove uwanted lines
    listArray = listArray[2:]
    return listArray
