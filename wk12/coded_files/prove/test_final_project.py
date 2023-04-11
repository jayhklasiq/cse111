from final_project import get_otp, number_list
import pytest
import random

import random

def test_get_otp():
    phonebook = {'208-274-2098', '208-892-9830', '208-426-1557'}
    phone_number = '208-274-2098'
    expected_otps = ['0SHT5', '78DHY', '46D7D', '5H5IW', 'EON38', '3HBOD', 'WGI39']
    for i in range(10):
        otp = get_otp(phonebook, phone_number)
        assert otp in expected_otps, f"Unexpected OTP generated: {otp}"


def test_number_list():
    # create a test file with phone numbers
    with open("test_numbers.txt", "wt") as file:
        file.write("208-274-2098\n208-892-9830\n208-426-1557\n")

    # test reading phone numbers from file
    expected_phonebook = ['208-274-2098', '208-892-9830', '208-426-1557']
    phonebook = number_list("test_numbers.txt")
    assert phonebook == expected_phonebook, f"Unexpected phone numbers: {phonebook}"

    # # test handling of missing file
    # try:
    #     phonebook = number_list("missing_file.txt")
    # except FileNotFoundError:
    #     pass
    # else:
    #     assert False, "Failed to raise FileNotFoundError"




pytest.main(["-v", "--tb=line", "-rN", __file__])

