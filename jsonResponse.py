# This class will handle execution of api call and optional parsing of response
import requests
import json

def executeJson (response, parse):
        
    if (response.ok):
        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(response.content)
        print("The response contains {0} properties".format(len(jData)))
        print("\n")
        
        if(parse):
            return parseJsonResponse(jData)
        else:
            return jData
    else:
        print("response failed: " + str(response))
               

def parseJsonResponse (response):
    resultsList =  {}
    
    for key in response:
            if (type(response[key]) is str):
                print (key + ":" + response[key])
                resultsList[key] = response[key]
            elif (type(response[key]) is int):
                print (key + ":" + str(response[key]))
                resultsList[key] = response[key]
            elif (type(response[key]) is dict):
                for dictKey in response[key]:
                    for innerDictKey in response[key][dictKey]:
                        print (dictKey + ":" + response[key][dictKey][innerDictKey])
                        resultsList[dictKey] = response[key][dictKey][innerDictKey]
                        
    return resultsList