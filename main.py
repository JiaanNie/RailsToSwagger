## import local package here
from ProcessRoutesFile import ProcessFile
from GenerateSwaggerElements import GenerateElements
from GenerateOutputFile import GenerateOutputFile
## main program flow start here

if __name__ == "__main__":
    routes_file = open("./RoutesFile/routes.txt", "r")
    output_file = open("./Output/Api.txt", "w")
    routes_dict = ProcessFile.Process(routes_file)
    swagger_elements = GenerateElements.Generate(routes_dict)
    GenerateOutputFile.Generate(swagger_elements, output_file)
