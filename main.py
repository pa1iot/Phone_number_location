import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode

key = 'a85b9168f0904c53b6c811bf81e1e8fc'

geocoder = OpenCageGeocode(key)
query = str(location)

result = geocoder.geocode(query)

print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

mymap = folium.Map(location=[lat,lng],zoom_start= 9)
folium.Marker([lat,lng],popup=location).add_to(mymap)

mymap.save("mylocation.html")
