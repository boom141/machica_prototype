import smtplib,random,string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, redirect,url_for,render_template,session,request,flash
# from confirmation_init import*
from datetime import date
from mongo_init import*
from settings import app

@app.route('/', methods=['POST','GET'])
def landing():
    if 'user' in session:
        if request.method == 'POST':
            query_email = request.form['email']
            query_msg = request.form['message']
            flash(' Your inquiry is sent, check your email for response')
            return redirect(url_for('inquiry', email=query_email, message=query_msg))
        else:
            return render_template('landing.html', user_in_session = session['user'][0].upper())
    else:
        if request.method == 'POST':
            query_email = request.form['email']
            query_msg = request.form['message']
            flash(' Your inquiry is sent, check your email for response')
            return redirect(url_for('inquiry', email=query_email, message=query_msg))
        else:
            return render_template('landing.html', user_in_session = None)
   

@app.route('/login', methods=['POST','GET'])
def login():
    if 'user' in session:
        return redirect(url_for('landing'))
    else:
        if request.method == 'POST':
            user_email = request.form['email']
            user_password = request.form['password']
            
            email_exist = machica_users.find_one({'email':user_email})
            password_exist = machica_users.find_one({'password':user_password})

            if email_exist and password_exist:
                session.permanent = True
                session['user'] = email_exist['first_name']
                return redirect(url_for('landing'))
            else:
                flash(' Your account is not registered yet.')
                return redirect(url_for('login'))

        else:
            return render_template('login.html',user_in_session = None)

@app.route('/register/<error>', methods=['POST','GET'])
def register(error):
    if 'user' in session:
        return redirect(url_for('landing'))
    else:
        if request.method == 'POST':
            session['firstname'] = request.form['first-name']
            session['lastname'] = request.form['last-name']
            session['gender'] = request.form['gender']
            session['phone_number'] = request.form['phone-number']
            session['registered_email'] = request.form['email']
            session['password' ]= request.form['password']
            session['confirm_password'] = request.form['confirm-password']

            generated_otp = ''
            for i in range(4):
                generated_otp += str(random.randint(0,9))

            session['gen_otp'] = generated_otp
            
            email_exist = machica_users.find_one({'email':session['registered_email']})
            if email_exist:
                flash(' Email is already taken, please use another email.')
                return redirect(url_for('register', error=401))
            elif session['password'] != session['confirm_password']:
                flash(' Password repeatition is not validated.')
                return redirect(url_for('register', error=402))
            else:
                return redirect(url_for('otp'))
                
        else:
            return render_template('register.html', user_in_session = None)

@app.route('/otp', methods=['POST','GET'])
def otp():
    if 'user' in session:
        return redirect(url_for('landing'))
    else:
        if request.method == 'POST':
            user_otp = request.form['user-otp']
            
            if 'gen_otp' in session:
                if user_otp == session['gen_otp']:

                    new_user = add_users(session['firstname'],session['lastname'],session['gender']
                    ,session['phone_number'],session['registered_email'],session['password'])
                    machica_users.insert_one(new_user)

                    flash('Your account is officially registered!')
                    return render_template('otp.html', user_in_session = None, email=session['registered_email'])

                else:
                    flash(' You entered a wrong OTP, try again')
                    return redirect(url_for('register', error=403))
            else:
                flash(' Something is wrong in geenrating otp, try again')
                return redirect(url_for('register', error=403))
        else:
            try:
                mail_content = f"YOU'RE OTP PIN IS: {session['gen_otp']}"
                #The mail addresses and password
                sender_address = 'otpsender47@gmail.com'
                sender_pass = 'xisnpznnkhkhcbls'
                receiver_address = session['registered_email']

                #Setup the MIME
                message = MIMEMultipart()
                message['From'] = sender_address
                message['To'] = receiver_address
                message['Subject'] = 'ONE TIME PIN REGISTRATION.'   #The subject line

                #The body and the attachments for the mail
                message.attach(MIMEText(mail_content, 'plain'))

                #Create SMTP session for sending the mail
                session_smtp = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                session_smtp.starttls() #enable security
                session_smtp.login(sender_address, sender_pass) #login with mail_id and password
                text = message.as_string()
                session_smtp.sendmail(sender_address, receiver_address, text)
                session_smtp.quit()
                print('Mail Sent')

                return render_template('otp.html', user_in_session = None, email=session['registered_email'])
            
            except:
                return redirect(url_for('register', error=False))

@app.route('/appointment', methods=['POST','GET'])
def appointment():  
    if 'user' in session:
        if request.method == 'POST':

            session['transaction_type'] = 'Booking'
            session['reference_id'] = get_referece_number()

            firstname = request.form['first-name']
            lastname = request.form['last-name']
            phone_number = request.form['phone-number']
            session['confirmation_email'] = request.form['email']
            date = request.form['date']
            time = request.form['time']
            session['entity_type'] = request.form['POA']
            msg = request.form['message']

            # remove the form checker**************
            if(not firstname and not lastname and not phone_number and not date and not time):
                flash(' You should check in on some of those fields above.')
                return render_template('appointment.html',  user_in_session = session['user'][0].upper())
            else:
                new_booking = add_booking(firstname,lastname,phone_number,session['confirmation_email'],date,time,session['entity_type'],msg if msg else None,session['reference_id'])
                machica_bookings.insert_one(new_booking)

                mail_content = Email_confirmation(session).generate_html()
                if smtp_transactions(session['transaction_type'],mail_content,'html'):
                    flash('Your booking has been confirmed. Check your email for details.')
                    return redirect(url_for('appointment'))
        else:
            return render_template('appointment.html',  user_in_session = session['user'][0].upper())
    else:
        return redirect(url_for('login'))

@app.route('/order', methods=['POST','GET'])
def order():
    if 'user' in session:
        if request.method == 'POST':

            session['transaction_type'] = 'Order'
            session['reference_id'] = get_referece_number()

            firstname = request.form['first-name']
            lastname = request.form['last-name']
            phone_number = request.form['phone-number']
            session['confirmation_email'] = request.form['email']
            session['entity_type'] = request.form['pr-name']
            quantity = request.form['quantity']
            msg = request.form['message']
            order_date = str(date.today())
            # remove the form checker**************
            if(not firstname and not lastname and not phone_number and not session['entity_type'] and not quantity):
                flash(' You should check in on some of those fields above.')
                return render_template('order.html',  user_in_session = session['user'][0].upper())
            else:
                new_order = add_orders(firstname,lastname,phone_number,session['confirmation_email'],session['entity_type'],quantity,msg if msg else None,session['reference_id'],order_date)
                machica_orders.insert_one(new_order)

                mail_content = Email_confirmation(session).generate_html()
                if smtp_transactions(session['transaction_type'],mail_content,'html'):
                    flash('Your order has been confirmed. Check your email for details.')
                    return redirect(url_for('order'))

        else:
            return render_template('order.html',  user_in_session = session['user'][0].upper())
    else:
        return redirect(url_for('login'))

def smtp_transactions(trsaction_type,mail_content,mail_type):
    try:
        #The mail addresses and password
        sender_address = 'inquirymachica20@gmail.com'
        sender_pass = 'meqfxsvprfyejvwn'
        receiver_address = session['confirmation_email']
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = trsaction_type   #The subject line
        
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, mail_type))
    
        #Create SMTP session for sending the mail
        session_confirm = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session_confirm.starttls() #enable security
        session_confirm.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session_confirm.sendmail(sender_address, receiver_address, text)
        session_confirm.quit()

        return True
    except: 
        return False

def get_referece_number():
    reference_number = ''
    for i in range(8):
        if random.randint(1,2) == 1:
             reference_number += random.choice(string.ascii_uppercase)
        else:
            reference_number += str(random.randint(0,9))
            
    return reference_number

@app.route('/admin/login', methods=['POST','GET'])
def admin_login():
    # if 'admin' in session:
    #     return redirect(url_for('admin_dashboard'))
    # else:
    #     if request.method == 'POST':
    #         email = request.form['email']
    #         password = request.form['password']
            
    #         admin_email_exist  =  machica_admins.find_one({'admin_email':email})
    #         admin_email_pass = machica_admins.find_one({'admin_password':password})

    #         if admin_email_exist and admin_email_pass :
    #             session['admin'] = 'admin'
    #             return redirect(url_for('admin_dashboard'))
    #         else:
    #             flash(' this admin account is not authorize.')
    #             return redirect(url_for('admin_login'))

    #     else:
    #         return render_template('admin-login.html')
    session['admin'] = 'admin'
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin' in session:
        return render_template('admin-dashboard.html')
    else:
        return redirect(url_for('landing'))

@app.route('/admin/booking')
def admin_booking():
    if 'admin' in session:
        return render_template('admin-booking.html')
    else:
         return redirect(url_for('landing'))

@app.route('/admin/order')
def admin_order():
    if 'admin' in session:
        return render_template('admin-order.html')
    else:
        return redirect(url_for('landing'))

@app.route('/logout')
def logout():
    session_keys = list(session)
    for key in session_keys:
        session.pop(key, None)

    return redirect(url_for('landing'))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

   
