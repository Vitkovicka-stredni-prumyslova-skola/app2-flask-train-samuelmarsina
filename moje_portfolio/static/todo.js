
const input = document.getElementById("inputTask");
const createBtn = document.querySelector('form input [type="button"]');
const inProcess = document.getElementById("inProcess");
const outProcess = document.getElementById("outProcess");

const span = document.createElement("span");
const br = document.createElement("br");

const inputCheckbox = document.createElement ("input");
inputCheckbox.type = "checkbox";

function addTask(text) {
    const span = document.createElement("span");
    const br = document.createElement("br");

    const inputCheckbox = document.createElement ("input");
    inputCheckbox.type = "checkbox";

    inProcess.appendChild(span);
    inProcess.appendChild(br);
    inProcess.appendChild(inputCheckbox);

    inputCheckbox.addEventListener("change", () => {
        const doneCheckBox = document.createElement("input");
        doneCheckBox.type = "checkbox";
        doneCheckBox.checked = true;

        const doneSpan = document.createElement("span");
        doneSpan.textContent = span.textContent;¨
        doneSpan.classList.add("done");

        const doneBr = document.createElement ("Br");

        outProcess.appendChild(doneCheckbox);
        outProcess.appendChild(doneSpam);
        outProcess.appendChild(doneBr);
}
)

createBtn.addEventListener("click", () => {
    console.log(input.value);
    addTask(input.value);
    input.value = "";
    input.focus();

});
