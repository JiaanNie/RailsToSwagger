def Format(routes_dict):
    for item in routes_dict:
        url_components_list =item["url"].split('/')
        for component in url_components_list:
            if "(.:format)" in component:
                location  = url_components_list.index(component)
                component = component[:component.find("(")]
                url_components_list[location] = component
            ## this for loop is use to remove (.:format) from the url
        for component in url_components_list:
            if ":" in component:
                location  = url_components_list.index(component)
                component = "{" + component[1:] + "}"
                url_components_list[location] = component
            ## this for loop is use to replcae : with {} from the url
        api_url ="/".join(url_components_list)
        item["url"] = api_url
    return routes_dict
