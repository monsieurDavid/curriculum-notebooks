var img = [];
var paths = ["images/coal.jpg","images/nat-gas.jpg","images/oil.jpeg","images/biofuel.jpg","images/geothermal.jpg","images/nuclear.jpg","images/solar.jpg"];
var headers = ["Coal","Natural Gas","Oil","Biofuel","Geothermal","Nuclear","Solar"]

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
    textFont("Helvetica");
    fill(255);
    noStroke();
    background(0);
    image(img[i],0,0);
    textSize(36)
    textStyle(BOLD)
    text(headers[i],7,405);
}