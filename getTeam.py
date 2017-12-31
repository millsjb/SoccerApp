# This class will house the api call to retrieve both fixture and general data about a given team.
import requests
import json
import jsonResponse

def getTeamInfo (team):
    url = "http://api.football-data.org/v1/teams/";
    url += team;
    
    print("url: "+ url)
    
    return formatTeamInfoResponse(jsonResponse.executeJson(requests.get(url), True))

def formatTeamInfoResponse (response):
    print ("formatTeamInfoResponse")
    formattedResponse = {}
    for key in response:
        formattedResponse[key] = response[key]
        
    return formattedResponse
        
