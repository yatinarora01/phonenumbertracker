import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+919971423311")

print("\n Phone Numbers LOcation \n")
print(geocoder.description_for_number(phone_number1,"en"));
