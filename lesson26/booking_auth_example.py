import requests


url = 'https://restful-booker.herokuapp.com/'
auth_info = {"username" : "admin",
    "password" : "password123"}
headers_cont_type_json = {'Content-Type': 'application/json'}

with requests.Session() as session:
    list_of_bookings = session.get(url+'booking')
    print(list_of_bookings.json())


def authentication_request(authrntication_data):
    responce= session.post(url+'auth', authrntication_data, headers_cont_type_json)
    return responce.json()

def create_booking():
    json_body = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    responce = session.post(url+'booking', headers_cont_type_json, json_body)
    return responce.json()

def change_booking():
    token = authentication_request(auth_info)
    headers = {'Content-Type': 'application/json'}
    headers['token']=token['token']
    json_body = {
    "firstname" : "Joahne",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    responce = session.post(url+'booking/1330', headers, json_body)
    return responce.json()

def change_booking_unauthorised():
    headers = {'Content-Type': 'application/json'}
    json_body = {
    "firstname" : "Joahne",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    responce = session.post(url+'booking/1330', headers, json_body)
    return responce.json()


def get_unexisting_object(object_id):
    try:
        response_body = session.get(url+f'booking/{object_id}')
        response_body.raise_for_status()
    except requests.exceptions.HTTPError as err:
        assert err.response.status_code == response_body.status_code


def create_booking_we_know_tou_not_work_pal():
    json_body = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    try:
        response_body = session.post(url+'booking', headers_cont_type_json, json_body)
        response_body.raise_for_status()
    except requests.exceptions.HTTPError as err:
        assert err.response.status_code == response_body.status_code