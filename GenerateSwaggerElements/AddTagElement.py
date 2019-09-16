def Add(attribute_dict):
    url = attribute_dict["url"]
    components_list = url.split("/")
    components_list = filter(None, components_list)
    tag = ''
    for index in range(len(components_list)-1, 0,-1):
        if "{" in components_list[index]:
            tag = ''
        else:
            tag = components_list[index]
            break
    attribute_dict["tag"] = tag
