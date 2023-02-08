import phonenumbers
import folium
from my_number import number
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import carrier

authentication_key = ["Add_your_token_in_here"]

sanNumber = phonenumbers.parse(number)
myLocation = geocoder.description_for_number(sanNumber, "en")
my_service_provider = phonenumbers.parse(number)

geocoder = OpenCageGeocode(authentication_key)

query = str(myLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup= myLocation).add_to((myMap))


print(myLocation)
print(carrier.name_for_number(my_service_provider, "en"))
print(results)
print(lat, lng)

myMap.save("location.html")