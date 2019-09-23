import requests
import json
import jsonpath


url  = "https://swapi.co/api/people/"

class fetchData():
    def data(self):
        request = requests.get(url)
        response = json.loads(request.text)
        person = jsonpath.jsonpath(response,"results")
        listName = []
        for i in person[0]:
            listName.append(i['name'])

        print("content : \n\n",request.content)
        print("headers : \n\n",request.headers)
        return listName