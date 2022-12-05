import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://MachicaDentalClininc:machica112@cluster0.rtavjlf.mongodb.net/?retryWrites=true&w=majority")

db = cluster['machica_db']

machica_users = db['machica_users']
machica_orders = db['machica_orders']
machica_bookings = db['machica_bookings']


def add_users(firstname,lastname,gender,phonenumber,email,password):

    user = {
        'first_name':firstname,
        'last_name': lastname,
        'gender': gender,
        'phone_number': int(phonenumber),
        'email': email,
        'password': password 
        }

    return user

def add_orders(firstname,lastname,phonenumber,email,product,quantity,msg):

    orders = {
        'first_name':firstname,
        'last_name': lastname,
        'phone_number': int(phonenumber),
        'email': email,
        'product': product,
        'quantity': quantity,
        'msg': msg,
        'payment_option': 'over the counter'
    }

    return orders


def add_booking(firstname,lastname,phonenumber,email,date,time,poa,msg):
    
    booking = {
        'first_name':firstname,
        'last_name': lastname,
        'phone_number': int(phonenumber),
        'email': email,
        'date': date,
        'time': time,
        'poa': poa,
        'msg': msg
    }

    return booking

