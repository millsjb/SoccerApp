function isBlank(val) {
	return (val == null || val == "" || val == "None");
}

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
	
	$("#league-table").html(htmlRow);
}