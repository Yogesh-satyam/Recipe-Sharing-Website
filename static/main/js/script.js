const menuBtn=document.querySelector(".menu-icon span");
const searchBtn=document.querySelector(".search-icon");
const cancelBtn=document.querySelector(".cancel-icon");
const items=document.querySelector(".nav-items");
const form=document.querySelector(".form");
const informationIcon = document.querySelector(".information");
const informationMessage = document.querySelector(".information-message");
menuBtn.onclick = ()=>{
  items.classList.add("active");
  menuBtn.classList.add("hide");
  searchBtn.classList.add("hide");
  cancelBtn.classList.add("show");
}
cancelBtn.onclick = ()=>{
 items.classList.remove("active");
 menuBtn.classList.remove("hide");
 searchBtn.classList.remove("hide");
 cancelBtn.classList.remove("show");
 form.classList.remove("active");
}
searchBtn.onclick=()=>{
  form.classList.add("active");
  searchBtn.classList.add("hide");
  cancelBtn.classList.add("show");
}

    
// Slider

const cuisibesContainers = [...document.querySelectorAll('.cuisines-container')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

cuisibesContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})

const handleClick = (event) => {
  informationMessage.classList.remove("hidden");
  informationMessage.classList.add("visible");
  setTimeout(() => {
    informationMessage.classList.add("hidden");
  },700);
}
informationIcon.addEventListener("mouseover",handleClick);

