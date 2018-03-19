# Flask file.
import jinja2
from flask import Flask, json, jsonify, render_template, request, make_response
from jinja2 import Environment, select_autoescape
from os.path import dirname
import constants, getApiData
from _operator import itemgetter
from operator import itemgetter
import ast
import json
import re

env = Environment(autoescape=select_autoescape(['html', 'xml']),
                  loader=jinja2.FileSystemLoader( dirname(__file__) + "/templates/" ))

app = Flask(__name__)

def getLeagueId(league):
    ID = None
    
    abrv = constants.leagueAbrv[league]
        
    jData = getApiData.getDataFromAllCompetitions()
    
    for data in jData:
        if(data["league"] == abrv):
            ID = data["id"]
            
#     print("Id: " + str(ID))
    
    return ID

def getTeamId(leagueId, team):
    teamID = None
    
    jData = getApiData.getTeam(leagueId)
        
    for data in jData["teams"]:
        if(team in data["name"]):
            matchObj = re.search(r'[0-9]+$', data["_links"]["self"]["href"])
            
            if(matchObj):
                teamID = matchObj.group()
            
    return teamID

def formatPlayerData(data):
    players = []
    
    for dict in data:        
        player = {}
        
        for key in dict:
            if(dict[key] is not None):
                player[key] = dict[key];
        
        players.append(player)
    
    return players

@app.route('/soccerapp/')
def index():
    return render_template( "home.html" )

@app.route('/soccerapp/league/')
@app.route('/soccerapp/league/<league>')
def getLeague(league=None):
    #if league is not provided, show normal league page with dropdown
    if(league==None):
        return render_template( "League.html", league="", table='""' )
        
    #get table and make sure it's valid json
    table = getTable(league)
                
    return render_template( "league.html", league=league, table=table )


@app.route('/soccerapp/team')
def getPlayersOfTeam():
    league  = request.args.get('league', None)
    teamName  = request.args.get('teamname', None)
    
#     print("league: " + league)
#     print("teamName: " + teamName)
    
    if(league==None or teamName==None):
        return render_template( "team.html", teamName="", players='""' )
    
    leagueID = getLeagueId(league)
    
    teamID = getTeamId(leagueID, teamName)
                
    data = getApiData.getTeamPlayers(teamID)
    
    return render_template( "team.html", teamName=teamName, players=formatPlayerData(data) )
    

@app.route('/soccerapp/get_table/<league>')
def getTable(league=None):
    table = []
    
    #retrieve league id
    leagueId = str(getLeagueId(league))
        
    data = getApiData.getLeagueTableInfo(leagueId)
        
    for key in data:
        row = {"Position": None, "Club": None, "Played": None, "Wins": None, "Drawn": None, "Lost": None}
        
        row["Position"] = key["position"]
        row["Club"] = key["teamName"]
        row["Played"] = key["playedGames"]
        row["Wins"] = key["wins"]
        row["Drawn"] = key["draws"]
        row["Lost"] = key["losses"]
        row["Points"] = key["points"]
        
        table.append(row)
        
    #Sorting by position, if needed
    table = sorted(table, key=lambda k: k["Position"])
    
    return json.dumps(table)

@app.route('/soccerapp/get_teams/<league>')
def getTeams(league=None):
    leagueId = getLeagueId(league)
    teams = []
    
    data = getApiData.getTeam(leagueId)
    
    for team in data["teams"]:
        teams.append(team["name"])
        
    return json.dumps(teams)

@app.route('/soccerapp/get_players', methods=['GET'])
def getPlayers():
    league  = request.args.get('league', None)
    teamName  = request.args.get('teamname', None)
        
    leagueID = getLeagueId(league)
    
    teamID = getTeamId(leagueID, teamName)
                
    data = getApiData.getTeamPlayers(teamID)
        
    return json.dumps(formatPlayerData(data))
        