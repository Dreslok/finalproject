
function updateSettings(){
    var thepuzimg;
    if (isPreset()){
        thepuzimg.src = document.querySelector('input[type=file]').files[0];
        var RsandCs = sendPresetVals();
        var imgsize = scalePic(thepuzimg.width, thepuzimg.height, myForm.presetimgsize.value);
    }
    else if (isCustom()){
        thepuzimg.src = document.querySelector('input[type=file]').files[0];
        var frack = sendCustomVals();
    }
    else{
        thepuzimg.src = JPizzle.jpg;
        rows = 5;
        columns = 5;
    }
}


function sendPresetVals(){
    var pv1 = myForm.presets.value;
    var pv2 = myForm.presetimgsize.value;
    var r = 0;
    var c = 0;
    var w = 0;
    var h = 0;
    if(pv1 == "2x2"){
        r = 2;
        c = 2;
    }
    if(pv1 == "4x6"){
        r = 4;
        c = 6;
    }
    if(pv1 == "5x5"){
        r = 5;
        c = 5;
    }
    if(pv1 == "6x4"){
        r = 6;
        c = 4;
    }
    if(pv1 == "8x12"){
        r = 8;
        c = 12;
    }
    if(pv1 == "10x10"){
        r = 10;
        c = 10;
    }
    if(pv1 == "12x8"){
        r = 12;
        c = 8;
    }
    if(pv1 == "12x16"){
        r = 12;
        c = 16;
    }
    if(pv1 == "16x12"){
        r = 16;
        c = 12;
    }
    if(pv1 == "16x20"){
        r = 16;
        c = 20;
    }
    if(pv1 == "20x16"){
        r = 20;
        c = 16;
    }
    if(pv1 == "20x20"){
        r = 20;
        c = 20;
    }
    
    return {rows: r, columns: c};

}

function scalePic(width, height, lsize){
    var w;
    var h;
    if (width >= height){
        w = lsize;
        h = lsize*(height/width);
    }
    else{
        w = lsize*(width/height);
        h = lsize;
    }
    return {width: w, height: h};
}

function sendCustomVals(){
    var r = myForm.rows.value;
    var c = myForm.columns.value;
    var w = myForm.width.value;
    var h = myForm.height.value;
    return {rows: r, columns: c, width: w, height: h};
}

function typeSelected(){
    var pt = myForm.ptype;
    if(pt && pt.length) {
        for(i = 0; i < pt.length; i++){
            if(pt[i] && pt[i].checked){
                return true;
            }
        }
    }
    return false;
}
function chooseTypeValues(){
    if (isPreset()){
        choosePresets();
    }
    else if (isCustom()){
        chooseCustom();
    }
}
function isPreset(){
    x = myForm.ptype.value;
    if (x == "ps") return true;
    else return false;
}
function isCustom(){
    x = myForm.ptype.value;
    if (x == "cs") return true;
    else return false;
}
function choosePresets(){
    document.getElementById("pset").style.visibility = "visible";
    document.getElementById("cstm").style.visibility = "collapse";

}
function chooseCustom(){
    document.getElementById("cstm").style.visibility = "visible";
    document.getElementById("pset").style.visibility = "collapse";
}



function addNewPic(){
    var preview = document.querySelector('img'); //selects the query named img
       var file    = document.querySelector('input[type=file]').files[0]; //sames as here
       var reader  = new FileReader();

       reader.onloadend = function () {
           preview.src = reader.result;
       }

       if (file) {
           reader.readAsDataURL(file); //reads the data as a URL
       } else {
           preview.src = "";
       }
}
function storeShit(){
    var pie;
    if(isPreset()){
        pie = sendPresetVals();
    }
    else if(isCustom()){
        pie = sendCustomVals();
    }
    else{
        pie = {rows: 5, columns: 5, width: 500, height: 500}
    }
    console.log(pie);
    localStorage.setItem("rows", pie.rows);
    localStorage.setItem("columns", pie.columns);
    localStorage.setItem("width", pie.width);
    localStorage.setItem("height", pie.height);
    puzzleImage = document.getElementById('puzzlimg');
    imgData = getBase64Image(puzzleImage);
    localStorage.setItem("imgData", imgData);
}
