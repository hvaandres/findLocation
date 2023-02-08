import phonenumbers
import folium
from my_number import number
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import carrier

key = ["Add_your_token_in_here"]

sanNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(sanNumber, "en")
service_provider = phonenumbers.parse(number)

geocoder = OpenCageGeocode(key)

query = str(yourLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup= yourLocation).add_to((myMap))


print(yourLocation)
print(carrier.name_for_number(service_provider, "en"))
print(results)
print(lat, lng)

myMap.save("location.html")