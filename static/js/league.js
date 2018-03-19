$(document).ready(function() {
	showTable(flaskVar.table);
});

if(isBlank(flaskVar.league)) {
	$("h1").hide();
}
else {
	$("#league-header").text(flaskVar.league);
}

$("#league-dropdown").change(function(t) {
	var dropdownVal = $("#league-dropdown").val();
	$("#league-header").text(dropdownVal).show();
	
	$.get("/soccerapp/get_table/" + dropdownVal, function(data, success) {
		showTable(JSON.parse(data));
	});
});






