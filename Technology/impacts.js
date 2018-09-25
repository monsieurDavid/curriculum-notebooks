var items = ["Increased standard of living","Climate change","Production of greenhouse gases","Extraction of resources","Economic growth","Increased job availability"]
var T = []
var pos = []
var c = 0
var tx
var ty = 0
var check = []
var value = 0
function setup() {
    createCanvas(700, 300);
    for (var i = 0; i < items.length; i++){
    	tx = 10
    	ty += 40
    	T[i] = new tbox(tx,ty,items[i],50,50,50)
    	check[i] = 'g'
    }

}

function draw() {
	background(255);
	for (var j = 0; j < text.length; j++){
		T[j].display();
		if (state && mouseX < T[j].X + 100 && mouseX > T[j].X - 40 && mouseY < T[j].Y + 10 && mouseY > T[j].Y - 10 && check[j] == 'g'){
			T[j].R = 60
			T[j].G = 209
			T[j].B = 53
			check[j] = 'r'
		}
		else if (state && mouseX < T[j].X + 40 && mouseX > T[j].X - 40 && mouseY < T[j].Y + 10 && mouseY > T[j].Y - 10 && check[j] == 'r'){
			T[j].R = 209
			T[j].G = 53
			T[j].B = 53
			check[j] = 'g'
		}
	}
}




function tbox(x,y,item,r,g,b) {
    this.X = x;
    this.Y = y;
    this.string = item
    this.R = r
    this.G = g
    this.B = b

tbox.prototype.display = function() {
    fill(this.R,this.G,this.B);
    noStroke();
    textSize(20)
    textStyle(BOLD)
    text(this.string,this.X,this.Y)
};

};

var state = false
function mousePressed() {
	state = true
 }
 function mouseReleased(){
 	state = false
 }