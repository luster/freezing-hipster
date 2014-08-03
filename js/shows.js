
var band = 'Time%20King';
var url = 'http://api.bandsintown.com/artists/'+band+'/events.json?api_version=2.0&app_id=tk-site'
var mos = ['January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'];

$.ajax({
    type: "GET",
    url: url,
    dataType: 'jsonp',
    success: function(d) {
        if (d.length == 0) {
            $("#tour-section").append("<h3>No shows at the moment.<br>Check back soon!</h3>");
            return;
        }
        //for (var i=0; i<d.length; i++) {
        for (var i=0; i<4; i++) {
            var date = d[i].datetime;
            var md = $.format.date(date, "MMMM d");
            var t = $.format.date(date, "h:mmp").replace(/\./g,'');
            var venue = d[i].venue.name;
            var loc = d[i].formatted_location;

            $("#tour-section").append('<h2>'+md+'</h2><h3>'+venue+'<br>'+loc+'<br>'+t+'<br><br>');
        }
        return;
    }
});
