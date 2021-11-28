// Scroll to top script
document.addEventListener("scroll", handleScroll);
// get a reference to our predefined button
var scrollToTopBtn = document.querySelector(".up");

function handleScroll() {
  var scrolled = window.pageYOffset;
  if (scrolled > 400) {
    //show button
    scrollToTopBtn.style.display = "block";
  } else {
    //hide button
    scrollToTopBtn.style.display = "none";
  }
}

scrollToTopBtn.addEventListener("click", scrollToTop);

function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}
// End of script

// Animate menu icon
function myFunction(x) {
  x.classList.toggle("change");
  var e = document.getElementById("nav");
  if (e.style.width == "180px") {
    e.style.width = "0px";
  } else {
    e.style.width = "180px";
  }
}