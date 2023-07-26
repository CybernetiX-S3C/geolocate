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
    print("To use the script, simply run the script and enter the phone number that you want to geolocate.")
    print("The script will then output the latitude and longitude of the mobile phone.")
    print("For example, to geolocate the phone number 123-456-7890, you would run the script as follows:")
    print("python geolocate.py 123-456-7890")
    print("")
    print("To get help, you can run the script with the -h or --help option.")

if __name__ == "__main__":
    print("Welcome to the geolocate tool!")
    print("To geolocate a phone number, simply enter the phone number and press Enter.")
    print("The script will then output the latitude and longitude of the mobile phone.")
    phone_number = input("Enter the phone number: ")
    latitude, longitude = geolocate(phone_number)
    print("The latitude is {}.".format(latitude))
    print("The longitude is {}.".format(longitude))
