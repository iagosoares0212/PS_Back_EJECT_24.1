
let count1 = 1;
document.getElementById("radio1").checked = true;

setInterval(function(){
    nextImage1();
}, 2000);

function nextImage1(){
    count1++;
    if(count1 > 5){  
        count1 = 1;
    }

    document.getElementById("radio" + count1).checked = true;
}

let count2 = 1;
document.getElementById("radio6").checked = true;

setInterval(function(){
    nextImage2();
}, 2000);

function nextImage2(){
    count2++;
    if(count2 > 5){  
        count2 = 1;
    }

    document.getElementById("radio" + (count2 + 5)).checked = true;
}
