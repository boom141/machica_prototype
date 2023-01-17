const get_booking_list = () =>{
    axios.get(`${window.origin}/admin/BookingList`)
    .then(res =>{
        if(res.data.length > 0){
            $('.loading-wrapper-3').fadeOut('slow')
            load_booking_list(res.data)
        }else{
            $('.loading-wrapper-3').fadeOut('slow')
            $('.empty-container-3').css('display','flex')
        }
    })
    .catch(error =>{
        console.log(error)
    })
}

const booking_section = document.getElementById('bookings-section-main')
const load_booking_list = (data) =>{
    const month_name = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
    ];

    while(booking_section.firstElementChild){
        booking_section.firstElementChild.remove()
    }
    
    for(book of data){
        let split_date = book['date'].split('-')
        $(booking_section).append(new booking_Block(split_date[2],month_name[parseInt(split_date[1])-1],book['poa'],book['time'],book['first_name'],book['last_name'],book['email'],book['reference_id']).render_html())
    }

    document.querySelectorAll('.booking-button').forEach(elem =>{
        elem.addEventListener('click', event =>{
            deleteAppointment(event.target.offsetParent.children[1].children[0].innerText)
        })
    })

}

const deleteAppointment = data =>{

    referenceId = data.split(':')[1].split('\n')[0]
    const formData = new FormData()
    formData.append('data', referenceId)

    axios.post(`${window.origin}/admin/deleteList`, formData)
    .then(res => {
        if(res.data === 'success'){
        window.location.reload()
        }
    })
    .catch(error => {
        console.log(error)
    })
}