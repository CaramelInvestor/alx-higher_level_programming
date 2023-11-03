#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""

from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""
    data = {"q": letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        response_data = response.json()
        if isinstance(response_data, dict) and "id" in response_data and "name" in response_data:
            print(f"[{response_data['id']}] {response_data['name']}")
        else:
            print("Not a valid JSON")
    except ValueError:
        print("No result")
