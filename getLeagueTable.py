# This class will house the api call to retrieve both fixture and general data about a given team.
import requests
import json
import jsonResponse

def getLeagueTableInfo (id):
    resultsList = {}
    url = "http://api.football-data.org/v1/competitions/";
    url += id + "/leagueTable";
    
    print("In getLeaguetable")
    
    return formatLeagueTableInfoResponse(jsonResponse.executeJson(requests.get(url), False))
        
    
def formatLeagueTableInfoResponse (response):
    print ("formatTeamInfoResponse")
    formattedResponse = None
    
    for key in response:
        if(key) == "standing":
            formattedResponse = response[key]
    
    if(formattedResponse is not None):   
        return formattedResponse
    else:
        print("Invalid response: missing standings")
