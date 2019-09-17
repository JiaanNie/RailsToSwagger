# the purpose of this function it will return model name and params list as return value

def  __GenerateModelName__(file_path):
    current_folder = file_path.split("\\")
    current_folder = current_folder[8:]
    dimmer = "_"
    model_name = dimmer.join(current_folder)
    return model_name

def __GenerateParamsList__(file_path):

    start_reading = False
    file = open(file_path, "r")
    for line in file:
        # if start_reading == True:
        #     print(line)
        if ( "#" in line and "PUT" in line ) or ( "#" in line and "POST" in line ):
            print(line)

def Generate(file_name, file_path):
    model_name = __GenerateModelName__(file_path)
    __GenerateParamsList__(file_path)
    #print(file_path)
