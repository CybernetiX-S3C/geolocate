import requests
import phonenumbers

def geolocate(phone_number):
    url = "https://api.phonenumbers.com/v2/phonenumbers/{}/geolocation".format(phone_number)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["latitude"], data["longitude"]
    else:
        return None

if __name__ == "__main__":
    phone_number = input("Enter the phone number: ")
    e164_format = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
    latitude, longitude = geolocate(e164_format)
    print("The latitude is {}.".format(latitude))
    print("The longitude is {}.".format(longitude))
