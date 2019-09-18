def Add(attribute_dict):
    body_request = {}
    if attribute_dict["method"] != "get" and attribute_dict["method"] != "delete":
        body_request["required"] = "true"
        body_request["ref"] = "#/components/schemas/"
    attribute_dict["body_request"] = body_request
