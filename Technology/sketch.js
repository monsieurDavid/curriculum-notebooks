var img = [];
var paths = ["images/coal.jpg","images/nat-gas.jpg","images/oil.jpeg","images/geothermal.jpg","images/nuclear.jpg","images/solar.jpg"];
var headers = ["Coal","Natural Gas","Oil","Geothermal","Nuclear","Solar"]
var body = ["Coal is one of the 3 types of fossil fuels and is considered to be a sedimentary rock. This means that over many centuries, deceased organic material experienced vast amounts of pressure and temperatures that transformed it into a solid state. We obtain energy from coal by combusting it to heat up water, which in turn creates steam, where the steam then turns a turbine generating electricity. ","Natural gas is another type of fossil fuel however, in a gaseous state as the name suggests. Much like coal and oil, it is formed through centuries of continous pressure and intense heat, eventually breaking down organic material into light, gaseous 'hydrocarbons'. Hydrocarbons are simply compounds that contain both hydrogen and carbon. They too are combusted to generate energy in a steam turbine.","Oil (petroleum) is the final type of fossil fuel, and is the most consumed source of energy for the entire planet.  This liquid substance is so versatile because it can be broken down into several different components via a process known as fractional distillation. Like the other fossil fuels, oil products are combusted to operate a steam turbine. Fossil fuels together make up over two thirds of the planet's energy consumption.","Deep within the core of our Earth the temperatures can reach temperatures as  warm as the surface of the Sun (5430 celsius). By either extracting liquid deep within the surface or pumping it down to these extreme temperatures, the process of bringing the hot liquid to the cooler surface causes it to condense into steam. As with most thermal energy generation methods, the steam will then turn a turbine to provide electricity. ","Nuclear fission is the process in which the nucleus of an atom splits into two smaller, new nuclei. This process releases a tremendous amount of energy/heat at such a small scale and is the foundation for modern nuclear energy generation. This heat is then used to convert water to steam thus generating power via a turbine.","There exists two types of solar energy generation. One is with the use of voltaic cells which converts solar energy directly to electrical energy. However, other solar farms exist where all the panels in a large area are directed towards a collection tower as shown in the image, where this heat is collected and used to heat water and eventually generate electricity with a steam turbine."]

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
    text(headers[i],7,400);
    textSize(14);
    textStyle(NORMAL);
    text(body[i],10,410,640,100);
    
}