import lesson26.booking_auth_example




def test_check_auth_data():
    responce = lesson26.booking_auth_example.authentication_request(lesson26.booking_auth_example.auth_info)
    print(responce)

def test_dreate_single_object():
    response = lesson26.booking_auth_example.create_booking()
    print(response)


def test_change_booking():
    response = lesson26.booking_auth_example.change_booking()
    print(response)


def test_change_booking_unauthorised():
    response = lesson26.booking_auth_example.change_booking_unauthorised()
    print(response)


def  test_nonexisting_object():
    lesson26.booking_auth_example.get_unexisting_object(94943953962)

def test_try_to_create_booking_and_fail():
    lesson26.booking_auth_example.create_booking_we_know_tou_not_work_pal()
