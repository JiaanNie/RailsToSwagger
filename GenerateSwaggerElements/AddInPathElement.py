
def __ExtraParams__(param):
    requirement_dict = {}
    requirement_dict["name"] = param[1:-1]
    requirement_dict["description"] = param[1:-1]
    requirement_dict["required"] = "true"
    if "id" in param:
        requirement_dict["type"] = "integer"
        requirement_dict["example"] = "123"
    else:
        requirement_dict["type"] = "string"
        requirement_dict["example"] = "abc"
    return requirement_dict

def Add(attribute_dict):
    in_path =[]
    param_obj = {}
    url_components_list = attribute_dict["url"].split("/")
    url_components_list = url_components_list[1:]
    for item in url_components_list:
        if item[0] == '{':
            param_obj = __ExtraParams__(item)
            in_path.append(param_obj)
    attribute_dict["in_path"] = in_path
