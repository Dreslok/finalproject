
function updateSettings(){
    var thepuzimg = Image;
    var rows;
    var columns;
    var width;
    var height;
    if (isPreset()){
        thepuzimg.src = document.querySelector('input[type=file]').files[0];
        var RsandCs = sendPresetVals();
        rows = RsandCs.rows;
        columns = RsandCs.columns;
        var imgsize = calcSize(myForm.presetimgsize.value);
        width = imgsize.width;
        height = imgsize.height;
    }
    else if (isCustom()){
        thepuzimg.src = document.querySelector('input[type=file]').files[0];
        var frack = sendCustomVals();
        rows = frack.rows;
        columns = frack.columns;
        width = frack.width;
        height = frack.height;
    }
    else{
        thepuzimg.src = 'JPizzle.jpg';
        rows = 8;
        columns = 6;
        width = 420;
        height = 666;
    }
    document.getElementById("viewVars").innerHTML = "Rows: " + rows + " Columns: " + columns + " Width: " + width + " Height: " + height + "";
    console.log(thepuzimg);
    console.log(thepuzimg.src);
    return {image: thepuzimg.src, rows: rows, columns: columns, width: width, height: height};
}

function calcSize(imgsize){
    var imgsrc = document.getElementById("preview");
    var imgwidth = imgsrc.width;
    var imgheight = imgsrc.height;
    var newwidth;
    var newheight;

    if (imgsize == "orgsz"){
        newwidth = imgwidth;
        newheight = imgheight;
    }
    else if (imgsize == "hlfsz"){
        newwidth = imgwidth/2;
        newheight = imgheight/2;
    }
    else{
        if (imgwidth >= imgheight){
            newwidth = imgsize;
            newheight = ((imgheight/imgwidth)*imgsize);
        }

        else{
            newheight = imgsize;
            newwidth = ((imgwidth/imgheight)*imgsize);
        }
    }
    console.log('imgwidth: '+ imgwidth + 'imgheight: ' + imgheight);
    console.log("newwidth: " + newwidth + "newheight: " + newheight);
    return{width: newwidth, height: newheight};
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
           preview.src = "JPizzle.jpg";
       }
}
