import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        country = geocoder.country_name_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")
        print(f"Country: {country}")
        print(f"Carrier: {carrier_name}")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Invalid phone number")
