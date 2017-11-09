# This class will house the basic underlying logic for the application.

import constants

print("Hello and welcome to millsjb Soccer Application")
print("")

league = raw_input("What league would you like to select?  ")

team = raw_input("What team would you like to see the most recent info for?  ")

if (team is None and team != ""):
    print("Thanks, please wait for " + team + "'s info.")
    
# selected_league = null #used for constants file TEMP
# 
# for l in constants.leagues:
#     if(l.contains(league)):
#         selected_league = l
#         
# print(selected_league)



if("bundesliga" in league):
    team = constants.bundesliga_teams[team]
if("premier" in league):
    team = constants.premier_league_teams[team]
    
    
# now call the function to build the url and make the appropriate api call
response = getTeamInfo(team)