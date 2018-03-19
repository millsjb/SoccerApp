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
    
    for data in response:
        print("response[data]: " + str(data))
        
        if(type(data) is dict):
            for dictKey in data:
                if(type(data[dictKey]) is str):
                    resultsList[dictKey] = response[data][dictKey]
                elif(type(data[dictKey]) is int):
                    resultsList[dictKey] = response[data][dictKey]
                elif(type(data[dictKey]) is dict):
                    for innerDictKey in data[dictKey]:
                        for innerDictKey in response[data][dictKey]:
                            resultsList[dictKey] = response[data][dictKey][innerDictKey]
        else:
            if(type(response[data]) is str):
                resultsList[data] = response[data]
            elif(type(response[data]) is int):
                resultsList[data] = response[data]
            elif(type(response[data]) is dict):
                for dictKey in response[data]:
                    for innerDictKey in response[data][dictKey]:
                        resultsList[dictKey] = response[data][dictKey][innerDictKey]
            elif(type(response[data]) is list):
                for innerVal in response[data]:
                    if(type(innerVal) is dict):
                        for dictKey in innerVal:
                            resultsList[dictKey] = innerVal[dictKey]
                    
    return resultsList