var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

canvas.width  = window.innerWidth - 100;
canvas.height  = window.innerHeight - 100;

var block = {
    // x : 10,
    // y : 200,
    // width : 50,
    // height : 50,
    draw(x, y, width, height, color){
        ctx.fillStyle = color;
        ctx.fillRect(x, y, width, height);
    }
    
}
var point = {
    x : 350,
    y : 100,
    width : 50,
    height : 50,
    draw(){
        ctx.fillStyle = 'green';
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
}
var player = {
    x : 10,
    y : 100,
    width : 50,
    height : 50,
    draw(){
        ctx.fillStyle = 'red';
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
}
point.draw()
block.draw(10, 200, 50, 1000, 'blue')
block.draw(10, 10, 1000, 50, 'blue')
block.draw(150, 10, 50, 600, 'blue')
block.draw(10, 700, 1000, 50, 'blue')
block.draw(300, 200, 50, 1000, 'blue')
player.draw()

var lastDownTarget;

window.onload = function doKeyDown(e) {
    

    document.addEventListener('S', function(event) {
        if(lastDownTarget == canvas) {
            alert('keydown');
        }
    }, false);
}