var img = [];
var paths = ["images/coal.jpg","images/nat-gas.jpg","images/oil.jpeg","images/biofuel.jpg","images/geothermal.jpg","images/nuclear.jpg","images/solar.jpg"];

// textFont("Helvetica");
// text("Attention, please.", 50, 200);
var button;
var i;
function setup() {
    createCanvas(650, 500);
    button = select('button');
    button.mousePressed(moveIndx);
    for (var j = 0; j < paths.length; j++) {
        img[j] = loadImage(paths[j]);
    }
    i = 0;
}
function moveIndx() {
    i += 1;
    if (i > paths.length - 1) {
        i = 0
    }
}
function draw() {
    background(0);
    image(img[i],0,0);
}