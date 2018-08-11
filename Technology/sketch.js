// var img = [];
// var paths = ["coal.jpg","sun.jpg","solar.jpg"];

// textFont("Helvetica");
// text("Attention, please.", 50, 200);
var bcolor = [0,50,100,150,200,250];
var button;
var i;
function setup() {
    createCanvas(700, 400);
    button = select('button');
    button.mousePressed(moveIndx);
    i = 0;
}
function moveIndx() {
    i += 1;
    if (i > bcolor.length - 1) {
        i = 0
    }
}
function draw() {
    background(bcolor[i]);
}