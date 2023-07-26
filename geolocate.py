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

def help():
    print("This script can be used to geolocate a phone number.")
    print("To use the script, simply enter the phone number that you want to geolocate.")
    print("The script will then output the latitude and longitude of the mobile phone.")
    print("For example, to geolocate the phone number 123-456-7890, you would enter:")
    print("python geolocate.py 123-456-7890")
    print("")
    print("To get help, you can run the script with the -h or --help option.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == "-h" or sys.argv[1] == "--help":
        help()
    else:
        phone_number = input("Enter the phone number: ")
        e164_format = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
        latitude, longitude = geolocate(e164_format)
        print("The latitude is {}.".format(latitude))
        print("The longitude is {}.".format(longitude))
