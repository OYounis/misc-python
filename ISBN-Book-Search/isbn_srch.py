import requests
import json

def isbn_srch (isbn, create_json = False, json_name = False,
            url = "https://openlibrary.org/api/books?", bibkeys = "isbn:", params = {"jscmd": "data", "format": "json"}):
    
    isbn = str(isbn).replace("-", "")

    request = {**{"bibkeys": bibkeys + isbn}, **params}
    data = requests.get(url, params = request)

    json_dict = json.loads(data.text)
    
    if (create_json == True):

        if (json_name == False):
            json_name = isbn
        elif (json_name == "title"): 
            json_name = json_dict["isbn:"+isbn]["title"]
        elif (json_name == "title+isbn"):
            json_name = json_dict["isbn:"+isbn]["title"] + isbn
        elif (json_name == "isbn+title"):
            json_name = isbn + json_dict["isbn:"+isbn]["title"]
        else:
            json_name = str(json_name)
                      
        with open(str(json_name) + ".json", "w+") as file_handle:
            print(json.dumps(json_dict, sort_keys = True, indent = 2), file = file_handle)

    return json_dict