// Buffalos buffalo Buffalo :: James Yu, Sadi Nirloy
// SoftDev pd8
// K27 -- Basic functions in JavaScript
// 2023-04-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn
function fib (n){
    if (n < 2){
        return n;
    }
    else{
        return fib(n - 1) + fib(n - 2);
    }
}

function fact (n){
    if (n < 2){
        return 1;
    }
    else{
        return n * fact(n - 1);
    }
}

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
