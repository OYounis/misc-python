from isbn_srch import isbn_srch as srch
from json import dumps

while True:
    search = input("isbn: ")
    if search == "quit":
        print("quitting isbn search....")
        break
    data = srch(isbn = search, create_json = True, json_name = "isbn+title")

    print (data)