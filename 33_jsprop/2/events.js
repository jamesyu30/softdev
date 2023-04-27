// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td');//elements in the table
var trs = document.getElementsByTagName('tr');//each row in the table
var table = document.getElementsByTagName('table')[0];//the table

var clicky = function(e) {
  alert( this.innerHTML );
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

table.addEventListener('click', clicky);


// Q: When user clicks on a cell, in what order will the pop-ups appear?
//PREDICTION: td then tr then the table
//we were right :)