def Swap(routes_file):
    #swap item1 to item2 and item2 to item 1
    for entry in routes_file:
        item1 = entry[0]
        item2 = entry[1]
        entry[0] = item2
        entry[1] = item1
    routes_file.sort()
    return routes_file
