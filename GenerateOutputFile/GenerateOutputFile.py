import GenerateBodyRequest
import GenerateContentHeader
import GenerateContentInPath
import GenerateFileHeader
import GenerateDefaultResponses
import GenerateModelsDefination



def Generate(swagger_elements, output_file):
    GenerateFileHeader.Generate(output_file)
    finish_entry = None
    for entry in swagger_elements:
        finish_entry =  GenerateContentHeader.Generate(output_file, entry, finish_entry)
        GenerateContentInPath.Generate(output_file, entry["in_path"])
        GenerateBodyRequest.Generate(output_file, entry["body_request"], entry["method"], entry["model_definition"])
        GenerateDefaultResponses.Generate(output_file, entry["responses"])
    GenerateModelsDefination.Generate(output_file, swagger_elements)
