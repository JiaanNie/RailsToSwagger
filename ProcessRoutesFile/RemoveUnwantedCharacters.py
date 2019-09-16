def Remove(routes_list, character):
    i  = 0
    while(i < 3 ):
        for route in routes_list:
            for element in route:
                if element == character:
                    route.remove(element)
        i = i + 1
    return routes_list
