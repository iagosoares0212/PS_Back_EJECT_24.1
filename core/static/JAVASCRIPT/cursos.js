let count = 1;
document.getElementById("radio1").checked = true;

setInterval( function() {
    nextImage();

}, 5000)

function nextImage () {
    
    count++;
    if(count>4) {
        count = 1
    }
    document.getElementById("radio"+count).checked=true;
}




window.addEventListener('DOMContentLoaded', (event) => {
   
    const carrossel = document.querySelector(".carrossel");
    if (carrossel) { 
        const firstCarWidth = carrossel.querySelector(".card").offsetWidth + 130;
        const arrowBtns = document.querySelectorAll(".wrapper button");

        arrowBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                
                carrossel.scrollLeft += btn.id === "left" ? -firstCarWidth : firstCarWidth ;
            });
        });
    }
});


window.addEventListener('DOMContentLoaded', (event) => {
   
    const carrossel = document.querySelector(".carrossel-second");
    if (carrossel) { 
        const firstCarWidth = carrossel.querySelector(".card-second").offsetWidth + 60;
        const arrowBtns = document.querySelectorAll(".wrapper-second #right2, .wrapper-second #left2");

        arrowBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                
                carrossel.scrollLeft += btn.id === "left2" ? -firstCarWidth : firstCarWidth ;
            });
        });
    }
});

window.addEventListener('DOMContentLoaded', (event) => {
   
    const carrossel = document.querySelector(".carrossel-third");
    if (carrossel) { 
        const firstCarWidth = carrossel.querySelector(".card-third").offsetWidth + 60;
        const arrowBtns = document.querySelectorAll(".wrapper-third #right3, .wrapper-third #left3");

        arrowBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                
                carrossel.scrollLeft += btn.id === "left3" ? -firstCarWidth : firstCarWidth ;
            });
        });
    }
});


window.addEventListener('DOMContentLoaded', (event) => {
   
    const carrossel = document.querySelector(".carrossel-fourth");
    if (carrossel) { 
        const firstCarWidth = carrossel.querySelector(".card-fourth").offsetWidth + 60;
        const arrowBtns = document.querySelectorAll(".wrapper-fourth #right4, .wrapper-fourth #left4");

        arrowBtns.forEach(btn => {
            btn.addEventListener("click", () => {     
                carrossel.scrollLeft += btn.id === "left4" ? -firstCarWidth : firstCarWidth ;
            });
        });
           
    }
});



document.addEventListener('DOMContentLoaded', function() {
    const carrossel = document.querySelector(".carrossel-student");
    let isDragging = false, startX, startScrollLeft;

    const dragStart = (e) => {
        isDragging = true;
        carrossel.classList.add("dragging")

        startX = e.pageX;
        startScrollLeft = carrossel.scrollLeft;
    }

    const dragging = (e) => {
        if(!isDragging) return;
        carrossel.scrollLeft = startScrollLeft - (e.pageX - startX);
        
    }

    const dragStop = () => {
        isDragging = false;
        carrossel.classList.remove("dragging")
    }

    carrossel.addEventListener("mousedown", dragStart);
    carrossel.addEventListener("mousemove", dragging)
    document.addEventListener("mouseup", dragStop)
});

window.addEventListener('DOMContentLoaded', (event) => {
   
    const carrossel = document.querySelector(".carrossel-student");
    if (carrossel) { 
        const firstCarWidth = carrossel.querySelector(".card-student").offsetWidth + 60;
        const arrowBtns = document.querySelectorAll(".wrapper-student #right5, .wrapper-student #left5");

        arrowBtns.forEach(btn => {
            btn.addEventListener("click", () => {     
                carrossel.scrollLeft += btn.id === "left5" ? -firstCarWidth : firstCarWidth ;
            });
        });
           
    }
});