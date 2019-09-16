def Add(attribute_dict):
    standard_responses = {"200": "OK", "204": "OK - no content", "400": "Forbidden", "404": "Not Found"}
    attribute_dict["responses"] = standard_responses
