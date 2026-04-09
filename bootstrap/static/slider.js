const slider = document.getElementById("slider");
let index = 0;

setInterval(() => {
    index++;

    if (index > 2) {
        index = 0;
    }

    slider.style.transform = `translateX(-${index * 100}%)`;
}, 3000); 