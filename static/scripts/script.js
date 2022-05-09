const buttonEL = document.querySelector(".button-overlay");
const overlayEL = document.querySelector(".overlay");
buttonEL.addEventListener("click", function () {
  overlayEL.classList.add(`hidden`);
});
