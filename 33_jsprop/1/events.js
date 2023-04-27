// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td');

var clicky = function(e) {
  alert( this.innerHTML ); //makes a popup of the elements inside the table that we click
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}
//adds eventListener to every element inside the table