$(document).ready(function() {	
	$("#team-header").html(flaskVar.teamName);
	
	showPlayers(flaskVar.players);
	
	$("#league-dropdown").change(function() {				
		// populate the teams dropdown
		$.get("/soccerapp/get_teams/" + $("#league-dropdown").val(), function(data, success) {			
			var dropdown = $("#team-dropdown");
			
			dropdown.empty();
			dropdown.append(
			        $('<option></option>').val('').html('Choose a team..')
			);
			
			_.each(JSON.parse(data), function(val) {
			    dropdown.append(
			        $('<option></option>').val(val).html(val)
			    );
			});
		});
	});

	$("#team-dropdown").change(function() {
		$.get("/soccerapp/get_players?league=" + $("#league-dropdown").val() 
				+ "&teamname=" + $("#team-dropdown").val(), function(data, success) {	
			if(success) showPlayers(JSON.parse(data));
		});
	});
	
});

function showPlayers(players) {
	keepers = [];
	defenders = [];
	midfielders = [];
	forwards = [];
	
	console.log(typeof players);
	
	_.each(players, function(player) {
		if(player['position'].includes('Keeper'))
			keepers.push(player);
		else if(player['position'].includes('Back'))
			defenders.push(player);
		else if(player['position'].includes('Midfield'))
			midfielders.push(player);
		else if(player['position'].includes('Forward'))
			forwards.push(player);
	});
	
	htmlRow = "<tr><th>GoalKeepers</th></tr>";
	_.each(keepers, addPlayerToTable);
	$("#goalkeepers").html(htmlRow);
	
	htmlRow = "<tr><th>Defenders</th></tr>";
	_.each(defenders, addPlayerToTable);
	$("#defenders").html(htmlRow);
	
	htmlRow = "<tr><th>Midfielders</th></tr>";
	_.each(midfielders, addPlayerToTable);
	$("#midfielders").html(htmlRow);
	
	htmlRow = "<tr><th>Forwards</th></tr>";
	_.each(forwards, addPlayerToTable);
	$("#forwards").html(htmlRow);
	
}

function addPlayerToTable(player) {
	htmlRow += "<tr>";
	htmlRow += "<th>" + player.name + "</th>";
	htmlRow += "</tr>";
}


