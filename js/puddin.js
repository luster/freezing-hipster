
q = [
    "Who you callin turkey?",
    "For your health",
];

var l = q.length;
var i = Math.floor(Math.random() * l);
document.getElementById("comment").placeholder = q[i];
