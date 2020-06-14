const toDoForm = document.querySelector(".js-toDoForm"),
    toDoInput = toDoForm.querySelector("input"),
    toDoList = document.querySelector(".js-toDoList");
    
const TODOS_LS = "toDos";

let toDos = [];

function deleteTodo(event) {
    const btn = event.target;
    const li = btn.parentNode;
    toDoList.removeChild(li);
    let cnt = 1;
    let newLiId;

    const cleanToDos =  toDos.filter(function(toDo) {
        if (toDo.id !== li.id) {
            newLiId = document.querySelector(`#${toDo.id}`);
            toDo.id = "n" + cnt;
            newLiId.id = "n" + cnt;
            ++cnt;
            return toDo;
        }
    });
    toDos = cleanToDos;
    saveToDos();
}

function saveToDos() {
    localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
}

function paintToDo(text) {
    const li  =  document.createElement("li");
    const delBtn = document.createElement("button")
    const span = document.createElement("span");
    const newId = toDos.length + 1;
    span.innerText = text;
    delBtn.innerText= "Delete";
    delBtn.addEventListener("click", deleteTodo);
    li.appendChild(span);
    li.appendChild(delBtn);
    toDoList.appendChild(li);
    li.id = "n" + newId
    const toDoObj = {
        text : text,
        id : "n" + newId
    };
    toDos.push(toDoObj);
    saveToDos();
}

function handleSubmit(event) {
    event.preventDefault();
    const currentValue = toDoInput.value;
    paintToDo(currentValue);
    toDoInput.value = "";
}
function loadToDos() {
    const loadedToDos = localStorage.getItem(TODOS_LS);
    if (loadedToDos !== null) {
        const parsedToDos = JSON.parse(loadedToDos);
        parsedToDos.forEach(function(toDo) {
            paintToDo(toDo.text);
        });
    }
}

function init() {
    loadToDos();
    toDoForm.addEventListener("submit", handleSubmit)
}

init();