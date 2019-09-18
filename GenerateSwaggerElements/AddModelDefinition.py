
def __GenerateModelDefinitionName__(url):
    name = url.split("/")
    name = name[1:]
    dimmeter =""
    for i in range(len(name)):
        if "*" in name[i]:
            name[i] = name[i][1:]
        if "_" in name[i] and "{" in name[i]:
            name[i] = name[i][1:-1]
            temp = name[i].split("_")
            for j in range(len(temp)):
                temp[j] = temp[j].capitalize()
            temp = dimmeter.join(temp)
            name[i] = temp
        elif "_" in name[i]:
            temp = name[i].split("_")
            for j in range(len(temp)):
                temp[j] = temp[j].capitalize()
            temp = dimmeter.join(temp)
            name[i] = temp
        elif "{" in name[i]:
            name[i] = name[i][1:-1]
            name[i] = name[i].capitalize()
        else:
            name[i] = name[i].capitalize()
    name = dimmeter.join(name)
    return name
def Add(attribute_dict):
    if attribute_dict["body_request"] != {}:
        attribute_dict["model_definition"] =  __GenerateModelDefinitionName__(attribute_dict["url"])
    else:
        attribute_dict["model_definition"] = ""
