

function chooseCustom(){
    chooseRowLength();
    chooseColumnLength();
    chooseWidth();
    chooseHeight();
}

function chooseRowLength(){
    document.getElementById("test").innerHTML = "ROW SHIT";
}

function chooseColumnLength(){
    var x = document.getElementById("test").innerHTML;
    document.getElementById("test").innerHTML = x+"COLUMN SHIT";
}

function chooseWidth(){
    var x = document.getElementById("test").innerHTML;
    document.getElementById("test").innerHTML = x+"WIDTH SHIZZ";
}

function chooseHeight(){
    var x = document.getElementById("test").innerHTML;
    document.getElementById("test").innerHTML = x+"HEIGHT SHIZZZZZZLE";
}


function choosePresets(){
    document.getElementById("test").innerHTML = "CHOOSE FROM A LIST MOFOS";
}

function uploadPhoto(){
    document.getElementById("test").innerHTML = "PICTURE UPLOAD TIME";

}

function getPuzShit(r,c,w,h){
    var pie = {rows: r, columns: c, width: w, height: h};
    return pie;
}