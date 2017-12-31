# This class will house the basic underlying logic for the application.

import constants, getTeam, getLeagueTable

print("Hello and welcome to Fixture Predictor!! The soccer app that puts your soccer knowledge to the test")
print("This app creates competition out of competition by allowing you, the user, to predict both weekly fixture outcomes " +
      "and overall league standings and then compares your guesses against the actual results.")
print("")
print("(In future) You can challenge your friends either on a weekly basis, or set up leagues to determine an overall champion.")

league = None
team = None
leagueId = None
apiCall = None
answer = None

while (answer is None or answer == ""):
    print("What info would you like to see?")
    answer = input("Please choose from the following options: [team info|league standings]")
    
if(answer == "team info"):
    while (league is None or league == ""):
        league = input("What league would you like to select?  ")
    
    while (team is None or team == ""):
        team = input("What team would you like to see the most recent info for?  ")
    
    if (team is not None and team != ""):
        print("Thanks, please wait for " + team + "'s info.")
    
    #retrieve team id from constants file
    if("bundesliga" in league):
        team = constants.bundesliga_teams[team]
    if("premier" in league):
        team = constants.premier_league_teams[team]
    
    # make api call  
    print(getTeam.getTeamInfo(team))
        
elif(answer == "league standings"):
    while (league is None or league == ""):
        league = input("What league would you like to select?  ")
        
    #retrieve team id from constants file
    if("bundesliga" in league):
        leagueId = "452"
    if("premier" in league):
        leagueId = "445"
    
    # make api call    
    print(getLeagueTable.getLeagueTableInfo(leagueId))
        
else:
    print("That option is not supported at this time.")

# done for now