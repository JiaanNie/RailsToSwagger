def Generate(output_file,  current_attributes_dict, previous_attributes_dict):
    current_url = ""
    current_url =   current_attributes_dict["url"]
    if previous_attributes_dict == None:
        output_file.write("  " + current_url + ":\n")
        output_file.write("    " + current_attributes_dict["method"]+":\n")
        output_file.write("      tags: ['" + current_attributes_dict["tag"]+ "']\n")
        output_file.write('      summary: "' + current_attributes_dict["purpose"] + '"\n')
        if current_attributes_dict["has_path_params"] == "true":
            output_file.write("      parameters:\n" )

    else:
        previous_url= ""
        previous_url = previous_attributes_dict["url"]
        if current_url != previous_url:
            output_file.write("  " + current_url + ":\n")
            output_file.write("    " + current_attributes_dict["method"]+":\n")
            output_file.write("      tags: ['" + current_attributes_dict["tag"]+ "']\n")
            output_file.write('      summary: "' + current_attributes_dict["purpose"] + '"\n')
            if current_attributes_dict["has_path_params"] == "true":
                output_file.write("      parameters:\n" )
        else:
            output_file.write("    " + current_attributes_dict["method"]+":\n")
            output_file.write("      tags: ['" + current_attributes_dict["tag"]+ "']\n")
            output_file.write('      summary: "' + current_attributes_dict["purpose"] + '"\n')
            if current_attributes_dict["has_path_params"] == "true":
                output_file.write("      parameters:\n" )

    return  current_attributes_dict
