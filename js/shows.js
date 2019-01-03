
$(document).ready(function(){
    var url = 'https://rest.bandsintown.com/artists/Time%2520King/events?app_id=tk-site&date=upcoming'

    $.ajax({
        type: "GET",
        url: url,
        dataType: 'jsonp',
        success: function(d) {
            if (d.length == 0) {
                $("#tour-section").append("<h3>No shows at the moment.<br>Check back soon!</h3>");
                return;
            }
            for (var i=0; i<d.length; i++) {
                var date = d[i].datetime;
                var md = $.format.date(date, "MMMM d");
                var t = $.format.date(date, "h:mmp").replace(/\./g,'');
                var venue = d[i].venue.name;
                var loc = d[i].formatted_location;
                var tixref = d[i].ticket_url;

                var to_a = '<h2>'+ md + '</h2>';
		if (tixref !== null) to_a += '<h4><a href="' + tixref + '">Get tickets!</a></h4>';
		to_a += '<h3>' + venue + '<br>' + loc + '<br>' + t + '<br><br>';
                $("#tour-section").append(to_a);
            }
            return;
        },
        error: function(xhr, ajaxOptions, thrownError) {
            $("#tour-section").append("<h3>Try Again</h3>");
        }
    });
});
