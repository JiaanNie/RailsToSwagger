def Generate(output_file, in_path_params):
    for path_param in in_path_params:
        output_file.write("      - in: path\n" )
        output_file.write("        name: " + path_param["name"] +"\n" )
        output_file.write("        description: " + path_param["description"] +"\n" )
        output_file.write("        required: " + path_param["required"] +"\n" )
        output_file.write("        schema:\n" )
        output_file.write("          type: " + path_param["type"] +"\n" )
        output_file.write("        example: " + path_param["example"] +"\n" )
