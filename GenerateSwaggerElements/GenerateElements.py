import AddTagElement
import AddInPathElement
import AddInPathParamsElement
import AddBodyRequestParamsElement
import AddDefaultResponsesElement
def Generate(routes_dict):
    for each_route_dict in routes_dict:
        AddTagElement.Add(each_route_dict)
        AddDefaultResponsesElement.Add(each_route_dict)
        AddInPathElement.Add(each_route_dict)
        AddInPathParamsElement.Add(each_route_dict)
        AddBodyRequestParamsElement.Add(each_route_dict)
    return routes_dict
