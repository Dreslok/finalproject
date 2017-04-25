function puzSetup(){
    if(!isValidCustom()){
        alert("try again");
        return false;
    }
    if(!isValidPreset()){
        alert("try again");
        return false;
    }
    storeshit();
    return true;
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
    if(pv2 == "orgsz"){
        w = 4;
        h = 5;
    }
    if(pv2 != "orgsz"){
        w = pv2;
        h = pv2;
    }
    var pie = {rows: r, columns: c, width: w, height: h};
    return pie;
}
function sendCustomVals(){
    var r = myForm.rows.value;
    var c = myForm.columns.value;
    var w = myForm.width.value;
    var h = myForm.height.value;
    var pie = {rows: r, columns: c, width: w, height: h};
    return pie;
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

function isValidRxC(){
    if (myForm.presets.value){
        return true;
    }
    return false;
}
function isValidImgSize(){
    if (myForm.presetimgsize.value){
        return true;
    }
    return false;
}
function isValidCustom(){
    if (isPreset()){
        return true;
    }
    else if (isCustom() && isValidRow() && isValidColumn() && isValidWidth() && isValidHeight()){
        return true;
    }
    return false;
}
function isValidPreset(){
    if(isCustom()){
        return true;
    }
    else if(isPreset() && isValidRxC() && isValidImgSize()){
        return true;
    }
    return false;
}
function isValidRow(){
    if (myform.rows.value){
        return true;
    }
    return false;
}
function isValidColumn(){
    if (myform.columns.value){
        return true;
    }
    return false;
}
function isValidWidth(){
    if (myform.width.value){
        return true;
    }
    return false;
}
function isValidHeight(){
    if (myform.height.value){
        return true;
    }
    return false;
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
    if(isPreset()){
        var pie = sendPresetVals();
    }
    else if(isCustom()){
        var pie = sendCustomVals();
    }
    else{
        var pie = {rows: 5, columns: 5, width: 500, height: 500}
    }
    localStorage.setItem("rows", pie.rows);
    localStorage.setItem("columns", pie.columns);
    localStorage.setItem("width", pie.width);
    localStorage.setItem("height", pie.height);
    puzzleImage = document.getElementById('puzzlimg');
    imgData = getBase64Image(puzzleImage);
    localStorage.setItem("imgData", imgData);
}

function getBase64Image(img) {
    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;

    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);

    var dataURL = canvas.toDataURL("image/png");

    return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
}