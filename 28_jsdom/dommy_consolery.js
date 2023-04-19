// Buffalos buffalo Buffalo :: James Yu, Sadi Nirloy
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};
//adds 30 to the input

//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };
//o.name returns name

var addItem = function(text) {
  var list = document.getElementById("thelist"); //thelist is the id for the list in the html file
  var newitem = document.createElement("h1");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};
//adds a the text you input to the list
//despite changing the html in the console, the update does not appear in the page

var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li'); // it doesn't specify which list it removes from
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
function fib (n){
  if (n < 2){
      return n;
  }
  else{
      return fib(n - 1) + fib(n - 2);
  }
}

// FAC
function fact (n){
  if (n < 2){
      return 1;
  }
  else{
      return n * fact(n - 1);
  }
}

// GCD
function gcd (a,b){
  if(a == 0){
    return b;
  }
  if (b == 0){
    return a;
  }
  else{
    return gcd(b, a%b);
  }
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => { //it makes it act like a function without the funtion keyword
  // body
  retVal = param1+param2;
  return retVal;
};


