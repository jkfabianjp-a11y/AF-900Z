const searchInput =
document.getElementById("searchInput");

const cards =
document.querySelectorAll(".project-card");

searchInput.addEventListener("keyup", () => {

const value =
searchInput.value.toLowerCase();

cards.forEach(card => {

const title =
card.querySelector("h3")
.textContent
.toLowerCase();

if(title.includes(value)){

card.style.display="block";

}
else{

card.style.display="none";

}

});

});

const buttons =
document.querySelectorAll(".filter-btn");

buttons.forEach(button=>{

button.addEventListener("click",()=>{

document
.querySelector(".active")
.classList
.remove("active");

button.classList.add("active");

const filter =
button.dataset.filter;

cards.forEach(card=>{

if(
filter==="all" ||
card.dataset.category===filter
){

card.style.display="block";

}
else{

card.style.display="none";

}

});

});

});