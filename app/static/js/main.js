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

// For new resource form
$(document).on('submit','#resource-form', function(e) {
  e.preventDefault();
  $.ajax({
    type:'POST',
    url:'/resources/new',
    data:{
      title: $("#title").val(),
      file_type: $("#file_type").val(),
      link: $("#link").val()
    },
    success:function()
    {
      alert('New resource added successfully!');
    }
  })
});

// For new helper form
$(document).on('submit','#helper-form', function(e) {
  e.preventDefault();
  $.ajax({
    type:'POST',
    url:'/helpers/new',
    data:{
      name: $("#name").val(),
      email: $("#email").val(),
      phone: $("#phone").val(),
      role: $("#role").val(),
      circle: $("#circle").val(),
      zone: $("#zone").val()
    },
    success:function()
    {
      alert('New resource added successfully!');
    }
  })
});





