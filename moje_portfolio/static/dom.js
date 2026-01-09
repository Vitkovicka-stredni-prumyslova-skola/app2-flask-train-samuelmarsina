document.getElementById("popis").innerHTML = "Tento text jsme změnili pomocí DOM"

let result = document.getElementByIdTagName("p")
console.log(result)


const box = document.getElementById("box");
console.log(box);

//vlastnost textContent vloží text bez html značek
box.textContent = "Tady jsem vložil text pomocí <b>vlastnosti<b> text"
//vlastnost innerHTML vloží a aplikuje i html značky
box.innerHTML = "<h1>Tady jsem vložil nadpis...</h1><p>Za nadpisem budu mít"

box.style.backgroundColor = "lightgrey";

box.style.border = "2py solid black";

function mouseOverHandler(e) {
    box.style.backgroundColor = "green";
}

box.addEventListener("mouseover", mouseOverHandler);