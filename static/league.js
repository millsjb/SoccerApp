$(document).ready(function() {
	showTable(flaskVar.table);
});

if(isBlank(flaskVar.league)) {
	$("h1").hide();
}

if(!isBlank(flaskVar.league)) {
	$("#league-header").text(flaskVar.league);
}

$("#league-dropdown").change(function(t) {
	var dropdownVal = $("#league-dropdown").val();
	$("#league-header").text(dropdownVal);
	
	$.get("/soccerapp/get_table/" + dropdownVal, function(data, success) {
		showTable(JSON.parse(data))
	});
});

function showTable(table) {
	htmlRow = "<tr><th>Position</th><th>Club</th><th>Played</th>" +
	"<th>Won</th><th>Drawn</th><th>Lost</th><th>Points</th></tr>";

	_.each(table, function(row) {
	htmlRow += "<tr>";
	htmlRow += "<th>" + row["Position"] + "</th>";
	htmlRow += "<th>" + row["Club"] + "</th>";
	htmlRow += "<th>" + row["Played"] + "</th>";
	htmlRow += "<th>" + row["Wins"] + "</th>";
	htmlRow += "<th>" + row["Drawn"] + "</th>";
	htmlRow += "<th>" + row["Lost"] + "</th>";
	htmlRow += "<th>" + row["Points"] + "</th>";
	htmlRow += "</tr>";
	});
	
	$("#home-table").html(htmlRow);
}




