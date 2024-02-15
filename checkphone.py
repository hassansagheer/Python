import phonenumbers
import geocoder
from phonenumbers import geocoder

phone_number = phonenumbers.parse("+12024561111") # replace with your phone number
country = geocoder.description_for_number(phone_number, "en")
print(country)
