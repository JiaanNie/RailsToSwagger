# models = {
#     "model_name": ["param1", "param2"....],
#     "model_name": ["param1", "param2"....],
#     "model_name": ["param1", "param2"....],
# }
import GenerateModels
def Scrape(files_structure):
    models = {}
    for path in files_structure:
        for file in files_structure[path]:
            file_path  = path + "\\" + file
            GenerateModels.Generate(file, file_path)

    return None
