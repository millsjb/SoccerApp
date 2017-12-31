# This class will house the basic underlying logic for the application.

import constants, getTeam

print("Hello and welcome to Fixture Predictor!! The soccer app that puts your soccer knowledge to the test")
print("This app creates competition out of competition by allowing you, the user, to predict both weekly fixture outcomes " +
      "and overall league standings and then compares your guesses against the actual results.")
print("")
print("(In future) You can challenge your friends either on a weekly basis, or set up leagues to determine an overall champion.")

league = None
team = None

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
    
print("team id: " + team)
    
# now call the function to build the url and make the appropriate api call using the team id from above
responseData = getTeam.getTeamInfo(team)