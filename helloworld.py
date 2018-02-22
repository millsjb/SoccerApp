# Flask file.
import jinja2
from flask import Flask, json, jsonify, render_template, request, make_response
from jinja2 import Environment, select_autoescape
from os.path import dirname
import constants, getTeam, getLeagueTable
from _operator import itemgetter
from operator import itemgetter
import ast
import json

env = Environment(autoescape=select_autoescape(['html', 'xml']),
                  loader=jinja2.FileSystemLoader( dirname(__file__) + "/templates/" ))

app = Flask(__name__)

@app.route('/soccerapp/')
def index():
    return render_template( "home.html" )

@app.route('/soccerapp/get_table/<league>')
def getTable(league=None):
    leagueId = "none"
    table = []
    
    print(league)
    
    #retrieve team id from constants file
    if("Bundesliga" in league):
        leagueId = "452"
    elif("Premier" in league):
        leagueId = "445"
    elif("Serie" in league):
        leagueId = "456"
    elif("Primera" in league):
        leagueId = "455"
    
    data = getLeagueTable.getLeagueTableInfo(leagueId)
        
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

@app.route('/soccerapp/league/')
@app.route('/soccerapp/league/<league>')
def getLeague(league=None):
    #if league is not provided, show normal league page with dropdown
    if(league==None):
        return render_template( "League.html", league="", table='""' )
    
    #get table and make sure it's valid json
    table = getTable(league)
    
    print(table);
            
    return render_template( "league.html", league=league, table=table )


@app.route('/soccerapp/team/<teamname>')
def team(teamname):
    return "Team is %" % teamname

@app.route('/soccerapp/player/<leaguename>')
def show_player_stats(league):
    return "League is %" % league

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)