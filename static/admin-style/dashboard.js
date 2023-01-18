const get_total_status = () =>{
    axios.get(`https://machica-mt8nuxrcx-boom141.vercel.app/admin/totalMonthSold`)
    .then(res =>{
        load_sold_status(res.data)
        })
    .catch(error =>{
        console.log(error)
    })
}

const chart_orders = document.getElementById('admin-charts-orders')
const chart_bookings = document.getElementById('admin-charts-bookings')
const load_sold_status = (data) =>{
    const month_name = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
    ];

    while(chart_bookings.firstElementChild){
        chart_bookings.firstElementChild.remove()
    }
    $(chart_bookings).append(new Monthly_Sold(data['bookings_total'],'BOOKINGS', month_name[data['current_date']-1].toUpperCase()).render_html())

    while(chart_orders.firstElementChild){
        chart_orders.firstElementChild.remove()
    }
    $(chart_orders).append(new Monthly_Sold(data['total_orders'],'ORDERS', month_name[data['current_date']-1].toUpperCase()).render_html())

}



const get_today_schedule = () =>{
    axios.get(`https://machica-mt8nuxrcx-boom141.vercel.app/admin/DailyAppointments`)
    .then(res =>{
        if(res.data.length > 0){
            $('.loading-wrapper-2').fadeOut()
            load_today_schedule(res.data)
        }else{
            $('.loading-wrapper-2').fadeOut()
            $('.empty-container-1').css('display','flex')
        }
            
    })
    .catch(error =>{
        console.log(error)
    })

}

const booking_container = document.getElementById('booking-container')
const load_today_schedule = (user_data) =>{
    while(booking_container.firstElementChild){
        booking_container.firstElementChild.remove()
    }

    for(let data of user_data){
        $(booking_container).append(new Daily_Schedule(data['first_name'],data['last_name'],
        data['email'],data['poa'],data['time']).render_html())
    }

    finishAppointment(document.querySelectorAll('.book-today'))
    document.querySelectorAll('.btn-typ').forEach(elem =>{
        elem.addEventListener('click', event =>{
            $(event.target.offsetParent.children[0]).css('width', '100%')
            sessionStorage.setItem(event.target.offsetParent.children[1].children[0].innerText,event.target.offsetParent.children[5].children[1].innerText)
            
            for(let i=0; i<event.target.offsetParent.children.length; i++) {
                event.target.offsetParent.children[i].style.color = 'white'
            }
            
            event.target.style.cursor = 'auto'
    })
})
}

const finishAppointment = data =>{
    if(sessionStorage.length > 0){
       for(let selector of data){
            if (selector.children[1].children[0].innerText in sessionStorage){
                $(selector.children[0]).css('width', '100%')
                
                for(let i=0; i<selector.children.length; i++) {
                    selector.children[i].style.color = 'white'
                    selector.lastElementChild.style.cursor = 'auto'
                }

            }
       }
    }
}
