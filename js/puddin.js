
q = [
    "Nice Hoagie",
    "Puddin' Pops",
    "Jell-O Pudding",
    "More Hoagies For Me",
    "Zip Zop Zoobity Bop"
];

var l = q.length;
var i = Math.floor(Math.random() * l);
document.getElementById("comment").placeholder = q[i];
