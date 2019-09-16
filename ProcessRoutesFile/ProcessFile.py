import ConvertLineToList
import RemoveUnwantedCharacters
import SwapElement
import ConvertListToDict
import FormatURLAttribute
def Process(routes_file):
    routes_list = ConvertLineToList.Convert(routes_file)
    routes_list = RemoveUnwantedCharacters.Remove(routes_list, "|")
    routes_list = SwapElement.Swap(routes_list)
    routes_dict = ConvertListToDict.Convert(routes_list)
    routes_dict = FormatURLAttribute.Format(routes_dict)
    return routes_dict
