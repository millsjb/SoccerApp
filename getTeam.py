# This class will house the api call to retrieve data about a specific team.

def getTeamInfo (team):
    url = "http://api.football-data.org/v1/teams/";
    url += team;
    
