import phonenumbers     # pip install phonenumbers

# geocoder: to know the specific location to the phone number

from phonenumbers import geocoder

phoneNumber = phonenumbers.parse( "+919533116633" )

# This will print geolocation of phone number

print( geocoder.description_for_number( phoneNumber, 'en') )