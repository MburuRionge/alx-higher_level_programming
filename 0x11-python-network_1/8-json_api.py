#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. The letter must be sent in the variable q
If no argument is given, set q="", If the response body is properly JSON
formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise: Display Not a valid JSON if the JSON is invalid or 
Display No result if the JSON is empty
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    data_let = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=data_let)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
