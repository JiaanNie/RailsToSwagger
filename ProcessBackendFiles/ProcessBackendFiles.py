import FilesSearcher
import ModelsScraper

base_path = "C:\\Users\\nie209\\Desktop\\Projects\\API_Doc_Generator\\BackendServicesFiles\\api"
def Process():
    files_structure = FilesSearcher.Search(base_path)
    models = ModelsScraper.Scrape(files_structure)
    return models
