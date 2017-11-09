# This class will house the basic underlying logic for the application.

print ("Hello and welcome to millsjb Soccer Application");

team = input("What team would you like to see the most recent info for?");

if (team != null and team.isEmpty() == false):
    print("Thanks, please wait for " + team + "'s info.");

# now call the function to build the url and make the appropriate api call
response = getTeamInfo(team);