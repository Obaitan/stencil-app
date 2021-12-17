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


const config = {
  type: 'bar',
  data: data,
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  },
};

const labels = Utils.months({count: 7});
const data = {
  labels: labels,
  datasets: [{
    label: 'My First Dataset',
    data: [65, 59, 80, 81, 56, 55, 40],
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)'
    ],
    borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgb(201, 203, 207)'
    ],
    borderWidth: 1
  }]
};
