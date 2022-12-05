import smtplib,random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, redirect,url_for,render_template,session,request,flash
from mongo_init import*
from settings import app
session_register = {}

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
            session_register['firstname'] = request.form['first-name']
            session_register['lastname'] = request.form['last-name']
            session_register['gender'] = request.form['gender']
            session_register['phone_number'] = request.form['phone-number']
            session_register['user_email'] = request.form['email']
            session_register['password' ]= request.form['password']
            session_register['confirm_password'] = request.form['confirm-password']
            
            email_exist = machica_users.find_one({'email':session_register['user_email']})
            if email_exist:
                flash(' Email is already taken, please use another email.')
                return redirect(url_for('register', error=401))
            elif session_register['password'] != session_register['confirm_password']:
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
   
            if user_otp == session_register['otp']:

                new_user = add_users(session_register['firstname'],session_register['lastname'],session_register['gender']
                ,session_register['phone_number'],session_register['user_email'],session_register['password'])
                machica_users.insert_one(new_user)

                flash('Your account is officially registered!')
                return render_template('otp.html', user_in_session = None, email=session_register['user_email'])
            else:
                flash(' You entered a wrong OTP, try again')
                return redirect(url_for('register', error=403))

        else:
            try:
                generated_otp = ''
                for i in range(4):
                    generated_otp += str(random.randint(0,9))

                session_register['otp'] = generated_otp
                mail_content = f"YOU'RE OTP PIN IS: {generated_otp}"
                #The mail addresses and password
                sender_address = 'otpsender47@gmail.com'
                sender_pass = 'xisnpznnkhkhcbls'
                receiver_address = session_register['user_email']

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

                return render_template('otp.html', user_in_session = None, email=session_register['user_email'])
            
            except:
                return redirect(url_for('register', error=False))

@app.route('/appointment', methods=['POST','GET'])
def appointment():  
    if 'user' in session:
        if request.method == 'POST':
            firstname = request.form['first-name']
            lastname = request.form['last-name']
            phone_number = request.form['phone-number']
            email = request.form['email']
            date = request.form['date']
            time = request.form['time']
            poa = request.form['POA']
            msg = request.form['message']

            if(not firstname and not lastname and not phone_number and not date and not time):
                flash(' You should check in on some of those fields above.')
                return render_template('appointment.html',  user_in_session = session['user'][0].upper())
            else:
                new_booking = add_booking(firstname,lastname,phone_number,email,date,time,poa,msg if msg else None)
                machica_bookings.insert_one(new_booking)
                return redirect(url_for('confirm', sender='booking_route', data=new_booking['email']))
        else:
            return render_template('appointment.html',  user_in_session = session['user'][0].upper())
    else:
        return redirect(url_for('login'))

@app.route('/order', methods=['POST','GET'])
def order():
    if 'user' in session:
        if request.method == 'POST':
            firstname = request.form['first-name']
            lastname = request.form['last-name']
            phone_number = request.form['phone-number']
            email = request.form['email']
            product = request.form['pr-name']
            quantity = request.form['quantity']
            msg = request.form['message']

            if(not firstname and not lastname and not phone_number and not product and not quantity):
                flash(' You should check in on some of those fields above.')
                return render_template('order.html',  user_in_session = session['user'][0].upper())
            else:
                new_order = add_orders(firstname,lastname,phone_number,email,product,quantity,msg if msg else None)
                machica_orders.insert_one(new_order)
                return redirect(url_for('confirm', sender='order_route', data=new_order['email']))
        else:
            return render_template('order.html',  user_in_session = session['user'][0].upper())
    else:
        return redirect(url_for('login'))


@app.route('/inquiry/<email>/<message>')
def inquiry(email,message):

    mail_content = f'User {email} ask,{message}' 
    #The mail addresses and password
    sender_address = 'inquirymachica20@gmail.com'
    sender_pass = 'meqfxsvprfyejvwn'
    receiver_address = 'Jvragudo6@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'User Inquiry'   #The subject line
    
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
   
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('the mail was sent')

    return redirect(url_for('landing'))


@app.route('/email_confirmation/<sender>/<data>')
def confirm(sender,data):
    mail_content = f"""
            <html>
            <body>
                <p><b>Your {'Order' if sender == 'order_route' else 'Booking'} is confirmed</b><br>
                Have questions?.<br>
                Message us at <a href="Jvragudo6@gmail.com">Jvragudo6@gmail.com</a> 
                for more details.
                </p>
            </body>
            </html>
            """
    #The mail addresses and password
    sender_address = 'inquirymachica20@gmail.com'
    sender_pass = 'meqfxsvprfyejvwn'
    receiver_address = data
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = f"Machica {'Order' if sender == 'order_route' else 'Booking'}"   #The subject line
    
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))
   
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    if sender == 'order_route':
        flash('Your order has been confirmed. Check your email for details.')
        return redirect(url_for('order'))
    elif sender == 'booking_route':
        flash('Your booking has been confirmed. Check your email for details.')
        return redirect(url_for('appointment'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('landing'))


if __name__ == '__main__':
    app.run(debug=True) 
   
