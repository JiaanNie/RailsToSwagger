def Generate(output_file, models):
    output_file.write("components:\n")
    output_file.write("  schemas:\n")
    type= ""
    __RemoveDuplicatesFromList(models)

    for model_name in models:
        result = __ConvertListToCompleteString__(models[model_name])
        print(model_name)
        output_file.write("    " + model_name + ":\n")
        output_file.write("      type: 'object'\n")
        output_file.write("      required: " + result + "\n")
        output_file.write("      properties:\n")
        for param in models[model_name]:
            output_file.write("        " + param + ":\n" )
            if "id" in param:
                type = "integer"
            else:
                type ="string"
            output_file.write("          type: '" + type + "'\n")
            if "_at" in param:
                output_file.write("          format: 'date-time'\n")
