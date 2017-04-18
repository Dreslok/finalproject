

function fillPuz(rows,columns,width,height){
    var gid = 0;
    var puzzle = [];
    for(var i = 0; i < rows; i++){
        for (var j = 0; j < columns; j++){
            puzzle[gid] = makePiece(i,j,width,height,gid);

            gid++;
        }
    }
    return puzzle;

}

function makePiece(inx,iny,inwidth,inheight, ingroupid){
    var piece = {x: inx, y: iny, width: inwidth, height: inheight, groupid: ingroupid};
    return piece;
}

function getRelPos(piece){
    px = piece.x * piece.width;
    py = piece.y * piece.height;
    return [px,py];
}

function chooseRowLength(){

}

function chooseColumnLength(){

}

function chooseWidth(){

}

function chooseHeight(){

}

function choosePresets(){

}

function uploadPhoto(){

}

