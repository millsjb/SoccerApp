# This class will house the api call to retrieve both fixture and general data about a given team.
import requests
import json

def getTeamInfo (team):
    url = "http://api.football-data.org/v1/teams/";
    url += team;
    
    response = requests.get(url)
    
    if (response.ok):
        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(response.content)
        print("The response contains {0} properties".format(len(jData)))
        print("\n")
        for key in jData:
            if (type(jData[key]) is str):
                print (key + ":" + jData[key])
            elif (type(jData[key]) is dict):
                for dictKey in jData[key]:
                    for innerDictKey in jData[key][dictKey]:
                        print (dictKey + ":" + jData[key][dictKey][innerDictKey])
            
    print(response.status_code)
    print(response)

