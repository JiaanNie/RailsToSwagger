def Generate(output_file, responses):
    output_file.write("      responses:\n")
    for response in responses:
        output_file.write("        '"+ response+ "':\n")
        output_file.write("          description: '" +responses[response] +"'\n")
