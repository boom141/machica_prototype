var navbar = document.getElementById("navbar");
const nav_links = document.querySelectorAll('.mx-2')

function getCurrentURL () {
  return window.location.href
}

var sticky = navbar.offsetTop;

window.onscroll = function() {
  if (window.pageYOffset > 0) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }

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


function active_onscroll(index){
  for(let i=0; i<nav_links.length-2; i++){
    if(index === i){
      nav_links[i].style.color = '#77c0e3'
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
  window.location = `${window.origin}/login`
}


const services = document.querySelectorAll('.service-type')
const service_container = document.querySelector('.list-services')
const sub_service = document.createElement('div')

let current_index = -1

services.forEach((element,index) =>{
      element.addEventListener('click', ()=>{
          if(index !== current_index){
            expand_services(index)
            current_index = index
          }
          
      })
})
 
function expand_services(index){
    for(let i=0; i<services.length; i++){
      if(i === index){
        services[i].style.animationName = 'expand'
        services[i].classList.remove('service-hover')
        sub_service.classList.add('sub-service-attribute')

        while(sub_service.firstElementChild){
          sub_service.firstElementChild.remove()
        }

        for(let i=0;i<3;i++){
          $(sub_service).append(new service_details(`Service name ${i+1}`,null,1000).render_html())
        }
        
        $(services[i]).append(sub_service)
        service_container.style.display = 'flex'
        $('.divider-service').css('display', 'inline-flex')
        $('.bck-btn').css('display', 'block')
      }else{
        services[i].style.display = 'none'
      }
    }  
}



const back_btn = document.querySelectorAll('.bck-btn')

back_btn.forEach((element,index)=>{
  element.addEventListener('click', event =>{
    for(let i=0; i<services.length; i++){
      if(i === index){
        services[i].style.animationName = 'wrap'
        services[i].classList.add('service-hover')
        services[i].removeChild(sub_service)
      }else{
        service_container.style.display = 'grid'
        services[i].style.display = 'block'
        services[i].style.animationName = 'null'
      }
      $('.divider-service').css('display', 'none')
      $('.bck-btn').css('display', 'none')
    }
    let timeout = setTimeout(()=>{ services[index].style.animationName = 'null'; current_index=-1; clearTimeout(timeout)}, 1000);
  })
})

function redirect_booking(){
  window.location = window.origin + '/appointment'
}

const border_content = document.querySelectorAll('.border-content')
const about_border = document.querySelectorAll('.about_border')

$('.border-content').hover((e)=>{
  $(e.target.parentElement).css({'transform': 'translate(-50%, -50%)','transform': 'rotateY(-20deg)', 'transform': 'skewY(3deg)'})
  $(e.target).css({'transform': 'rotateY(20deg)', 'transform': 'skewY(-3deg)'})
},(e)=>{
  $(e.target.parentElement).css({'transform': 'translate(0%, 0%)','transform': 'rotateY(0deg)', 'transform': 'skewY(0deg)'})
  $(e.target).css({'transform': 'rotateY(0deg)', 'transform': 'skewY(0deg)'})
})

