const clockContainer = document.querySelector(".js-clock"),
 clockTitle = clockContainer.querySelector("h1");

function getTime() {
    const date = new Date();
    const minutes = date.getMinutes();
    const hours = date.getHours()
    let apm
    if (parseInt(hours/12) === 0){
        apm = "AM";
    }else if (parseInt(hours/12) === 1){
        apm = "PM";
    }
    const seconds = date.getSeconds();
    clockTitle.innerText = `${hours%12 < 10 ? `0${hours%12}` : hours%12}:${
        minutes < 10 ? `0${minutes}` : minutes} ${apm}`;

}

function init() {
    getTime();
    setInterval(getTime, 1000);
}

init();