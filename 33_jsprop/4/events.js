// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  //PREDICTION: the td will pop up only
  //only the td pops up when stopPropagation is uncommented, when it is uncommented the table will pop up first
  //e.stopPropagation();
};


//Q: Does the order in which the event listeners are attached matter?
//PREDICTION: no
//it doesn't

//Predict, then test...
//Q: What effect does the boolean arg have in each?
//   (Leave exactly 1 version uncommented to test...)
//PREDICTION: addEventListeners with true will be prioritized over the ones with false, and the smaller elements will be prioritized if there are multiple trues
//true will  be prioritized, but it goes from the bigger element to the smaller element in  case of a tie
//if it's false, the smaller element will have priority in a tie

//table.addEventListener('click', clicky, true);

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky, true);
  //tds[x].addEventListener('click', clicky, false);
}

for (x=0; x < trs.length; x++) {
  //trs[x].addEventListener('click', clicky, true);
  trs[x].addEventListener('click', clicky, false);
}

//table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false);
