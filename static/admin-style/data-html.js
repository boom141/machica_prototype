class User_Block{
    constructor(name,email,visibility){
        this.name = name
        this.email = email
        this.visibility = visibility

    }
    render_html(){
        return `<div class="user-block">
                    <div class="user-text" >
                        <strong style="font-size: .9rem; margin-top: rem;">${this.name}</strong>
                        <h6 style="font-size: .7rem;">${this.email}</h6>
                    </div>
                    <img style="pointer-events: none; display: ${this.visibility}" src="https://img.icons8.com/ios-glyphs/50/337c73/circled-right.png"/>
                </div>`
    }
}

class Monthly_Sold{
    constructor(total_sold,purchase_type,current_month){
        this.total_sold = total_sold
        this.purchase_type = purchase_type
        this.current_month = current_month
    }
    render_html(){
        return `<div class="number-purchase">
                <h1 style="font-size: 3.5rem; line-height: 3rem;">${this.total_sold}</h1>
                <h6 style="font-size: .8rem;">${this.purchase_type}</h6>
                </div>
                <span style="height: 100%; width: 1px; background-color: rgb(189, 189, 189);"></span>
                <p style="text-align: center; height: auto; padding-top: 1rem; line-height: 25px; ">As of the month <br> <span style="font-weight: 600; color: #337c73;">${this.current_month}</span> </p>`
    }
}


class Daily_Schedule{
    constructor(first_name,last_name,email,service_name,scheduled_time){
        this.first_name = first_name
        this.last_name = last_name
        this.email = email
        this.service_name = service_name
        this.scheduled_time = scheduled_time
    }
     render_html(){
        return `<div class="book-today">
                <div class="checker"></div>
                <div class="profile-section">
                    <strong>${this.first_name} ${this.last_name}</strong>
                    <h6>${this.email}</h6 >
                </div>
                <span style="height: 100%; width: 1px; background-color: rgb(189, 189, 189);"></span>
                <div class="profile-section">
                    <strong>Service Category</strong>
                    <h6>${this.service_name}</h6 >
                </div>
                <span style="height: 100%; width: 1px; background-color: rgb(189, 189, 189);"></span>
                <div class="profile-section">
                    <strong>Scheduled Time</strong>
                    <h6>${this.scheduled_time}</h6 >
                </div>
                <span style="height: 100%; width: 1px; background-color: rgb(189, 189, 189);"></span>
                <div class="btn-typ" style="margin-left: 1.5rem;"><img src="https://img.icons8.com/external-febrian-hidayat-glyph-febrian-hidayat/40/337c73/external-check-ui-essential-febrian-hidayat-glyph-febrian-hidayat.png"/></div>
            </div>`
     }     
}



class booking_Block{
    constructor(day,month,service_name,scheduled_time,first_name,last_name,email,referenceId){
        this.day = day
        this.month = month
        this.service_name = service_name
        this.scheduled_time = scheduled_time
        this.first_name = first_name
        this.last_name = last_name
        this.email = email
        this.referenceId = referenceId
    }   
    render_html(){
        return `<div class="book-today apt-block">
                    <div class="date-section">
                        <h1 style="color: white; font-size: 3.5rem; line-height: 3rem;">${this.day}</h1>
                        <h6 style="color: white; font-size: .8rem; font-weight:bold;">${this.month}</h6>
                    </div>
                    <div class="book-details">
                        <p style="font-weight: 600; font-size: 1.2rem; line-height: 1.5rem; width: auto;" >${this.service_name}:${this.referenceId} <br>
                            <span style="font-weight:300; font-size: 1rem;" >${this.first_name} ${this.last_name}: ${this.email}</span> <br>
                            <span style=" color: white; font-weight:300; font-size: .8rem; background-color: #337c73; padding: .3rem .3rem; border-radius: 20px;">${this.scheduled_time}</span>
                        </p>
                    </div>
                    <span style="height: 5rem; width: 1px; background-color: rgb(189, 189, 189);"></span>
                    <div class="booking-button">
                        <span style="color: white; font-weight: bold;">DELETE</span>
                        <img src="https://img.icons8.com/metro/26/FFFFFF/trash.png"/>
                    </div>
                </div>`
    }
}

class Order_Block{
    constructor(item_name,reference_code,first_name,last_name,email,quantity,date){
        this.item_name = item_name
        this.reference_code = reference_code
        this.first_name = first_name
        this.last_name = last_name
        this.email = email
        this.quantity = quantity
        this.date = date
            
    }
    render_html(){
        return `<div class="book-today apt-block">
                    <div class="date-section order-section">
                    <img style="height: 4rem; width: 4rem;" src="https://img.icons8.com/ios-filled/100/FFFFFF/tooth.png"/>
                    </div>
                    <div class="book-details">
                        <p style="font-weight: 600; font-size: 1.2rem; line-height: 1.5rem; width: auto;" >${this.item_name}:${this.reference_code} <br>
                            <span style="font-weight:300; font-size: 1rem;" >${this.first_name} ${this.last_name}: ${this.email}</span> <br>
                            <span style=" color: white; font-weight:300; font-size: .8rem; background-color: #337c73; padding: .3rem .3rem; border-radius: 20px;">${this.date} | ${this.quantity}</span>
                        </p>
                    </div>
                    <span style="height: 5rem; width: 1px; background-color: rgb(189, 189, 189);"></span>
                    <div class="booking-button">
                        <span style="color: white; font-weight: bold;">DELETE</span>
                        <img src="https://img.icons8.com/metro/26/FFFFFF/trash.png"/>
                    </div>
                </div>`
    }
}