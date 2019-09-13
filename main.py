## import local package here
from ProcessOriginalFile import ProcessFile
from GenerateOutputFile import GenerateFile
from ObtainRequiredAttributes import ObtainOpenAPIAttributes

## main program flow start here
if __name__ == "__main__":
    file_dict = ProcessFile.Process("routes.txt");
    file_dict = ObtainOpenAPIAttributes.Obtain(file_dict);
    GenerateFile.GenerateAPIDoc(file_dict);
