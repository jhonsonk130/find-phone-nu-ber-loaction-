import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim

# Initialize the geocoder
geolocator = Nominatim(user_agent="phone-number-locator")

def get_phone_number_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, "NP")

        location = geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")

        # Reverse geocoding to get precise location
        location_details = geolocator.geocode(location)

        return location_details, carrier_name

    except phonenumbers.phonenumberutil.NumberParseException:
        return None, None



phone_number = input("Enter the phone number: ")


location, region = get_phone_number_info(phone_number)

if location and region:
    print(f"Location: {location}")
    print(f"Region/Carrier: {region}")
    latitude = location.latitude
    longitude = location.longitude
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Region/Carrier: {region}")
   
else:
    print("Invalid phone number")
