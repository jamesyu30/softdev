var c = document.getElementById("playground");

var dotButton = document.getElementById("buttonCircle");

var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "cyan";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing = true;

var drawDot = () => {
    window.cancelAnimationFrame(requestID); //stops the Animaniac button from speeding up the circle
    clear();
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, 2*Math.PI);
    ctx.fill();
    ctx.closePath();

    if (radius == c.width/2){
        growing = false;
    }
    if (radius == 0){
        growing = true;
    }

    if (growing){
        radius++;
    }
    if (!growing){
        radius--;
    }

    requestID = window.requestAnimationFrame(drawDot); //pass in the function you want to animate
};

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);