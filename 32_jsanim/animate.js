/*
James Yu, Sadi Nirloy 
*/

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var screenButton = document.getElementById("dvdButton");

var ctx = c.getContext("2d");

var requestID;

var clear = (e) =>{
    e.preventDefault(); // To prevent some kind of unnecessary repetition
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 0;
var growing = true;
var smaller = Math.min(c.width, c.height);

var drawDot = () => {
    window.cancelAnimationFrame(requestID); // to prevent the acceleration of animation
    //clear(); makes an error (TypeError: Cannot read properties of undefined (reading 'preventDefault'))
    ctx.clearRect(0, 0, c.width, c.height);
    ctx.beginPath(); // A path is needed in order to isolate steps in coloring
    ctx.fillStyle = "black"; //circle color
    ctx.strokeStyle = "black"; // outline color
    ctx.arc(c.width / 2, c.height / 2, radius, 0, 2*Math.PI);
    ctx.fill();
    ctx.closePath();
    if (growing ){
        radius += 5;
    }else{
        radius -= 5;
    }

    if ( radius > smaller / 2 && growing){
        growing = false;
    }

    if (radius <= 0 && !growing){
        growing = true;
    }
    requestID = window.requestAnimationFrame(drawDot);
    //dotButton.removeEventListener("click", drawDot); // I used this method to take away the power of the button to add layers of animation.
    // I need to do this since this method needs to requestAnimationFrame itself at all times it is running, so I could not limit its access to that step.
}

var stopIt = () =>{
    window.cancelAnimationFrame(requestID);
    //dotButton.addEventListener("click", drawDot);
}

var dvdLogoSetup = function(){
    window.cancelAnimationFrame( requestID); // Uses the same requestID in order to have only "one animation" play at a time
    var rectWidth = 100;
    var rectHeight = 50;

    var rectX = Math.floor(Math.random() * (c.height - (2*rectHeight)));//so the logo doesn't go into the wall
    var rectY = Math.floor(Math.random() * (c.width - (2*rectWidth)));

    var xVel = Math.random() * 5;
    var yVel = Math.random() * 5;


    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        var count = 0;
        //clear(); makes an error (TypeError: Cannot read properties of undefined (reading 'preventDefault'))
        ctx.clearRect(0, 0, c.width, c.height)
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if (rectX <= 0 || rectX + rectWidth >= c.width){
            xVel *= -1;
        }
        if (rectY <= 0 || rectY + rectHeight >= c.height){
            yVel *= -1;
        }
        rectX += xVel;
        rectY += yVel;

        //checks if the logo hits the corner
        //bottom right
        if (rectY + rectHeight >= c.height && rectX + rectWidth >= c.width){
            count++;
        }
        //bottom left
        if (rectY + rectHeight >= c.height && rectX + rectWidth <= 0){
            count++;
        }
        //top right
        if (rectY + rectHeight <= 0 && rectX + rectWidth >= c.width){
            count++;
        }
        //top left
        if (rectY + rectHeight <= 0 && rectX + rectWidth <= 0){
            count++;
        }
        document.getElementById('count').innerHTML = count;
        requestID = window.requestAnimationFrame(dvdLogo);//dvdSetup makes the logo go VERY fast
    };
    dvdLogo();

}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup);