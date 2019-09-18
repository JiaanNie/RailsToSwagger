# the purpose of this function it will return model name and params list as return value

# def  __GenerateModelName__(file_path):
#     current_folder = file_path.split("\\")
#     current_folder = current_folder[8:]
#     dimmer = "_"
#     model_name = dimmer.join(current_folder)
#     return model_name[:-3]

def __GenerateParamsList__(file_path):
    models=  []
    current_endpoint = ""
    file = open(file_path, "r")
    for line in file:
        if ("PUT" in line and "#" in line) or ("POST" in line and "#" in line):
            current_endpoint = line
            models.append(current_endpoint)


def Generate(file_name, file_path):
    #model_name = __GenerateModelName__(file_path)

    ## i dont know how to genreate this
    model_name = __GenerateParamsList__(file_path)
    return model_name
