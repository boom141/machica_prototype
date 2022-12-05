var navbar = document.getElementById("navbar");
const nav_links = document.querySelectorAll('.mx-2')
let landing_urls = ['http://127.0.0.1:5000/', 'http://127.0.0.1:5000/#home', 
'http://127.0.0.1:5000/#about', 'http://127.0.0.1:5000/#services', 'http://127.0.0.1:5000/#products']


function getCurrentURL () {
  return window.location.href
}


for(let i=0; i<nav_links.length-2; i++){
  nav_links[i].addEventListener('click',()=>{
    if(!landing_urls.includes(String(getCurrentURL()))){
        window.location = landing_urls[0]
    }
  })
}


var sticky = navbar.offsetTop;

window.onscroll = function() {
  if (window.pageYOffset > 0) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }

  if(landing_urls.includes(String(getCurrentURL()))){
  if(window.pageYOffset >= 0 && window.pageYOffset < 600){
    active_onscroll(0)
  }else if (window.pageYOffset >=600 && window.pageYOffset < 1180){
    active_onscroll(1)
  }else if (window.pageYOffset >= 1180 && window.pageYOffset < 1790){
    active_onscroll(2)
  }else if (window.pageYOffset >= 1790 && window.pageYOffset < 2518){
    active_onscroll(3)
  }else{
    active_onscroll(-1)
  }
  }

};


function active_onscroll(index){
  for(let i=0; i<nav_links.length-2; i++){
    if(index === i){
      nav_links[i].style.color = '#7AC4E7'
    }else{
      nav_links[i].style.color = 'white'
    }
}
}


function appointment_page(){
  window.location = window.location.href
}


function order_page(){
  window.location = window.location.href
}

function login_page(){
  window.location = 'http://127.0.0.1:5000/login'
}