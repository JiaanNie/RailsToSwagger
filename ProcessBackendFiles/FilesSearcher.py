#object_structure = {
#     "path": ["file1","file2"....],
#     "path": ["file1","file2"...],
#     "path": ["file1","file2"....],
# }
import os
def Search(base_path):
    object_structure = {}
    for path, folders, files in os.walk(base_path):
        object_structure[path] = files
    return object_structure
