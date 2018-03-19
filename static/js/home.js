$(document).ready(function() {
	var dropdownVal = "Premier";
	$("#league-header").text(dropdownVal).show();
		
	$.get("/soccerapp/get_table/" + dropdownVal, function(data, success) {
		showTable(JSON.parse(data));
	});
});