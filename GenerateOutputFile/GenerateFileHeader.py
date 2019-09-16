def Generate(output_file):
    openAPIVersion = "3.0.0"
    infoTilte = "Message API"
    infoDescription = " API for Messaging microservice"
    infoVersion = "2017-11-30-alpha"
    servers = [
        {
            "url":"http://micro.cs.uregina.ca:3000/",
            "description": "Dev Server"
        },
        {
            "url":"http://micro.cs.uregina.ca:3001/",
            "description": "Optional Server, testing API doc spec"
        }
    ]

    output_file.write("openapi: "+openAPIVersion + "\n")
    output_file.write("info:\n")
    output_file.write("  "+"title: "+ infoTilte+"\n")
    output_file.write("  "+"description: "+ infoDescription+"\n")
    output_file.write("  "+"version: "+ infoVersion+"\n")
    output_file.write("servers:\n")
    for server in servers:
        output_file.write("  - "+"url: " + server["url"] + "\n")
        output_file.write("    "+"description: " + server["description"] + "\n")
    output_file.write("paths:\n")
