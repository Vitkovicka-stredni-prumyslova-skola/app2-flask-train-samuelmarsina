
const input = document.getElementById("inputTask");
const createBtn = document.querySelector('form input [type="button"]');
const inProcess = document.getElementById("inProcess");
const outProcess = document.getElementById("outProcess");

const span = document.createElement("span");
const br = document.createElement("br");

const inputCheckbox = document.createElement ("input");
inputCheckbox.type = "checkbox";

function addTask(text) {


    
}

createBtn.addEventListener("click", () => {
console.log(input.value);
input.value = "";
input.focus();

});
