/*function fillPuz(rows,columns,width,height){
    var gid = 0;
    var puzzle = [];
    for(var i = 0; i < rows; i++){
        for (var j = 0; j < columns; j++){
            puzzle[gid] = makePiece(i,j,width,height,gid);

            gid++;
        }
    }
    return puzzle;
}*/

function makePiece(ingroup, inpicPoint,ingroupid, inipos, injpos){
    var piece = {groups: [ingroup], picPoint: inpicPoint, groupid: ingroupid, ipos: [inipos], jpos: [injpos]};
    return piece;
}

function getRelPos(piece){
    px = piece.x * piece.width;
    py = piece.y * piece.height;
    return [px,py];
}
