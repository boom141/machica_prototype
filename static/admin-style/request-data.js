window.onload = () =>{
    get_user_list()
    get_today_schedule()
    get_total_status()
    get_booking_list()
    get_order_list()

}

const get_user_list = () =>{
    axios.get(`https://machica-mt8nuxrcx-boom141.vercel.app/admin/getUserList`)
    .then(res =>{
        if(res.data.length > 0){
            $('.loading-wrapper-1').fadeOut('slow', ()=>{
                load_user_data(res.data)
            })
        }else{
            $('.loading-wrapper-1').fadeOut('slow')
            $('.empty-container-2').css('display','flex')
        }
    })
    .catch(error =>{
        console.log(error)
    })
}

const get_user_history = (user) => {
    return axios.post(`https://machica-mt8nuxrcx-boom141.vercel.app/admin/userHistory`, user)
    .then(res => {
        return res.data
    })
    .catch(error => {
        console.log(error)
    })
}

const userBlock_container = document.getElementById('user-block-container')
const load_user_data = (user_data) =>{
    while(userBlock_container.firstElementChild){
        userBlock_container.firstElementChild.remove()
      }

    $(userBlock_container).css('display','flex')
    for(user of user_data){
        $(userBlock_container).append(new User_Block(user['first_name'],user['email'], 'block').render_html())
    }
    for(block of userBlock_container.children){
        block.addEventListener('click', userLogs)
    }
}

const userLogs = e =>{
    let historyUser = e.target.children[0].children[0].innerText
    let requestUser = e.target.children[0].children[1].innerText

    const formData = new FormData()
    formData.append('user', requestUser)
    
    $(userBlock_container).fadeOut('fast' ,()=>{
        $('.user-container').append(`<h5> <img onclick="hideLogs()" style="transform: scaleX(-1); cursor: pointer" src="https://img.icons8.com/ios-glyphs/50/337c73/circled-right.png"/>
        User: ${historyUser}'s activity logs</h5>`)
        
        get_user_history(formData).then(user_log_list =>{
            for(list of user_log_list){
                for(data of list){  
                    if('poa' in data)
                        $('.user-container').append(new User_Block(`Type:${data['poa']}`,`${data['time']} | ${data['date']}`, 'none').render_html())
                    else
                        $('.user-container').append(new User_Block(`Type:${data['product']}`,`${data['date']}`, 'none').render_html())
                }
                
            }
        })

    })
}

const hideLogs = () => {
    while(document.getElementById('user-container').firstElementChild){
        document.getElementById('user-container').firstElementChild.remove()
    }
    window.location.reload()
}


const find_btn = document.getElementById('find-btn')
const user_find = document.getElementById('user-find')
const not_found_ico = document.getElementById('not-found')

find_btn.addEventListener('click', event =>{
    event.preventDefault()
    const user_data = new FormData()
    user_data.append('user_email', user_find.value)

    while(user_container.firstElementChild){
        user_container.firstElementChild.remove()
    }

    axios.post(`https://machica-mt8nuxrcx-boom141.vercel.app/admin/getUserList`,user_data)
    .then(res =>{
        if(res.data !== null){
            $('.loading-wrapper-1').fadeOut('slow')
            $(user_container).append(new User_Block(res.data['first_name'],res.data['email']).render_html())
        }else{
            console.log('hello')
            $('.loading-wrapper-1').fadeOut('slow')
            not_found_ico.style.display = 'flex'
            $(user_container).append(not_found_ico)
        }
    })
    .catch(error =>{
        console.log(error)
    })
})

