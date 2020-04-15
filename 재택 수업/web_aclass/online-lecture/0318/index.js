const form = document.querySelector("form");
const input = form.querySelectorAll("input");

console.log(form, input)

function f(val) {
    return val.value !== null;
}

function handleSubmit(event) {
    event.preventDefault();
    console.log(input[1].value)
    if (input[0].value === ""){
        alert("사용자 이름을 입력하세요.")
    } else if (input[1].value === ""){
        alert("비밀번호를 입력하세요.")
    } else if (input[1].value.length < 8){
        alert("비밀번호를 8글자 이상 입력하세요.")
    } else if (input[2].value === ""){
        alert("비밀번호 확인을 입력하세요.")
    } else if (input[1].value !== input[2].value){
        alert("비밀번호가 일치하지 않습니다.")
    } else {
        alert("성공적으로 회원가입되었습니다.")
    }
    input[0].value = "";
    input[1].value = "";
    input[2].value = "";
}

function init() {
    form.addEventListener("submit", handleSubmit);
}

init();