def Add(attribute_dict):
    attribute_dict["has_path_params"] = "false"
    url_components_list = attribute_dict["url"].split("/")
    url_components_list = url_components_list[1:]
    for element in url_components_list:
        if element[0] == "{":
            attribute_dict["has_path_params"] = "true"
            break
