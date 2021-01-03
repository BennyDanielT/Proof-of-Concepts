import phonenumbers as PH
from phonenumbers import geocoder
from phonenumbers import carrier

number=input("Enter the Phone Number: ")

ch_number=PH.parse(number,"CH") #C-Country H-History

print(geocoder.description_for_number(ch_number,"en"))

service_number=PH.parse(number,"RO")

print(carrier.name_for_number(service_number,"en"))
