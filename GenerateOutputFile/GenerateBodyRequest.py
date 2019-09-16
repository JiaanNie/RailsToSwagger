def Generate(output_file, body_request, method):
    if body_request !=  {}:
        output_file.write("      requestBody:\n" )
        output_file.write("        required: " + body_request["required"] +"\n" )
        output_file.write("        content:\n" )
        output_file.write("          application/json:\n" )
        output_file.write("            schema:\n" )
        output_file.write("              $ref: '" + body_request["ref"] +"'\n" )
