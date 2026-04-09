const input = document.getElementById("inputTask");
const createBtn = document.querySelector('form input[type="button"]');
const inProcess = document.getElementById("inProcess");
const outProcess = document.getElementById("outProcess");
const clearDoneBtn = document.getElementById("clearDoneBtn");

function addTask(text) {
    const clean = text.trim();
    if (!clean) return;

    const row = document.createElement("div");

    const cb = document.createElement("input");
    cb.type = "checkbox";

    const span = document.createElement("span");
    span.textContent = clean;

    row.appendChild(cb);
    row.appendChild(span);
    inProcess.appendChild(row);

    cb.addEventListener("change", () => {
        if (cb.checked) {
            span.classList.add("done");
            outProcess.appendChild(row);
        } else {
            span.classList.remove("done");
            inProcess.appendChild(row);
        }

        if (inProcess.children.length === 0) {
            inProcess.innerHTML = "<i>Žádné úkoly v procesu</i>";
            inProcess.classList.add("none");
        } else {
            inProcess.getElementsByTagName("i")[0]?.remove();
            inProcess.classList.remove("none");
        }
    });
}


createBtn.addEventListener("click", () => {
addTask(input.value);
input.value = "";
input.focus();
});

input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        event.preventDefault();
        createBtn.click();
    }
});


clearDoneBtn.addEventListener("click", () => {
outProcess.innerHTML = "";
const result=confirm("Chcete opravdu smazat všechny dokončené úkoly?");
if (result) {
    alert("Všechny dokončené úkoly byly smazány.");
}
else {
    alert("Smazání dokončených úkolů bylo zrušeno.");
    }
});