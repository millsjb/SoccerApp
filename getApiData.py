# This class will house the api call to retrieve both fixture and general data about a given team.
import requests
import json
import jsonResponse

headers = {'X-Auth-Token': '0028d0d9a3554f72b77d6882eaa89681'}

def getAllCompetitions ():
    url = "http://api.football-data.org/v1/competitions"
        
    return formatCompetitionsResponse(jsonResponse.executeJson(requests.get(url, headers=headers), True))

def getDataFromAllCompetitions ():
    url = "http://api.football-data.org/v1/competitions"
        
    return jsonResponse.executeJson(requests.get(url, headers=headers), False)

def getTeam (leagueId):
    url = "http://api.football-data.org/v1/competitions/"
    url += str(leagueId) + "/teams"
    
    return jsonResponse.executeJson(requests.get(url, headers=headers), False)

def getTeamInfo (team):
    url = "http://api.football-data.org/v1/teams/"
    url += team
    
    print("url: "+ url)
    
    return formatTeamInfoResponse(jsonResponse.executeJson(requests.get(url, headers=headers), True))

def getTeamPlayers (team):
    url = "http://api.football-data.org/v1/teams/" + team + "/players"
    
    print("url: "+ url)
    
    return formatTeamPlayersResponse(jsonResponse.executeJson(requests.get(url, headers=headers), False))

def getLeagueTableInfo (id):
    resultsList = {}
    url = "http://api.football-data.org/v1/competitions/"
    url += id + "/leagueTable"
    
    print(url)
    
    return formatLeagueTableInfoResponse(jsonResponse.executeJson(requests.get(url, headers=headers), False))

def formatCompetitionsResponse (response):
    formattedResponse = {}
    return formattedResponse

def formatIDsResponse (response):
    formattedResponse = {}
    return formattedResponse

def formatTeamInfoResponse (response):
    formattedResponse = {}
    for key in response:
        if(key == "players"):
            formattedResponse = response[key]
        
    if(formattedResponse is not None):   
        return formattedResponse
    else:
        print("Invalid response: missing players")
        
def formatTeamPlayersResponse (response):
    formattedResponse = response["players"]
        
    return formattedResponse
            
        
def formatLeagueTableInfoResponse (response):
    print ("formatTeamInfoResponse")
    formattedResponse = None
    
    for key in response:
        if(key == "standing"):
            formattedResponse = response[key]
    
    if(formattedResponse is not None):   
        return formattedResponse
    else:
        print("Invalid response: missing standings")



        
